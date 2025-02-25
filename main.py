import serial
import time
import tkinter as tk
from tkinter import messagebox, ttk, filedialog, Menu
from ttkthemes import ThemedTk
import json
import os
import csv
from PIL import Image, ImageTk  # Use this import for older Pillow versions
from tkinter.ttk import Progressbar
import threading
from pymongo import MongoClient  # MongoDB integration


class FingerprintApp:
    def __init__(self, root):
        self.root = root
        self.registered_fingerprints = {}
        self.DATA_FILE = "fingerprints.json"

        # MongoDB connection
        self.client = MongoClient("mongodb://localhost:27017/")  # Connect to local MongoDB
        self.db = self.client["fingerprint_db"]  # Create/use a database
        self.collection = self.db["fingerprints"]  # Create/use a collection

        self.load_data()
        self.setup_serial()
        self.setup_gui()

    def setup_serial(self):
        try:
            self.arduino = serial.Serial(port='COM4', baudrate=9600, timeout=1)
        except serial.SerialException as e:
            messagebox.showerror("Serial Error", f"Error opening serial port: {e}")
            self.root.quit()

    def load_data(self):
        try:
            # Fetch all documents from the collection
            documents = self.collection.find({})

            # Convert documents to the registered_fingerprints dictionary
            self.registered_fingerprints = {
                doc["_id"]: {
                    "national_id": doc["national_id"],
                    "name": doc["name"],
                    "section": doc["section"],
                    "department": doc["department"],
                    "year": doc["year"],
                    "image_path": doc["image_path"]
                }
                for doc in documents
            }
            print("Data loaded from MongoDB.")
        except Exception as e:
            print(f"Error loading data from MongoDB: {e}")

    def save_data(self):
        try:
            # Clear the collection before saving new data
            self.collection.delete_many({})

            # Insert all fingerprints into the collection
            if self.registered_fingerprints:
                self.collection.insert_many([
                    {"_id": fingerprint_id, **data}  # Use fingerprint_id as _id
                    for fingerprint_id, data in self.registered_fingerprints.items()
                ])
            print("Data saved to MongoDB.")
        except Exception as e:
            print(f"Error saving data to MongoDB: {e}")

    def read_serial(self):
        if self.arduino.in_waiting > 0:
            return self.arduino.readline().decode('utf-8').strip()
        return None

    def read_fingerprint_id(self):
        data = self.read_serial()
        if data and data.isdigit():
            return int(data)
        return None

    def update_label(self):
        self.arduino.write(b'D')
        fingerprint_id = self.read_fingerprint_id()
        if fingerprint_id is not None:
            if fingerprint_id in self.registered_fingerprints:
                user_data = self.registered_fingerprints[fingerprint_id]
                self.label.config(text=f"Welcome, {user_data['name']}!", fg="green")
                self.fingerprint_image_label.config(image=self.verified_icon)

                # Display user image
                if user_data["image_path"] and os.path.exists(user_data["image_path"]):
                    try:
                        image = Image.open(user_data["image_path"])
                        image = image.resize((100, 100), Image.ANTIALIAS)  # Use Image.ANTIALIAS
                        user_image = ImageTk.PhotoImage(image)
                        self.user_image_label.config(image=user_image)
                        self.user_image_label.image = user_image  # Keep a reference
                    except Exception as e:
                        print(f"Error loading image: {e}")
            else:
                self.label.config(text=f"Unknown fingerprint ID: {fingerprint_id}", fg="red")
                self.fingerprint_image_label.config(image=self.unverified_icon)
        self.root.after(100, self.update_label)

    def register_fingerprint(self):
        name = self.name_entry.get().strip()
        national_id = self.national_id_entry.get().strip()
        section = self.section_entry.get().strip()
        department = self.department_entry.get().strip()
        year = self.year_entry.get().strip()
        image_path = self.image_path

        if not name or not national_id or not section or not department or not year:
            messagebox.showerror("Error", "Please fill all fields.")
            return

        self.arduino.write(b'E')
        messagebox.showinfo("Info", "Place your finger on the sensor to enroll.")
        self.progress_bar.start()
        self.status_bar.config(text="Enrolling fingerprint...")
        threading.Thread(target=self.enroll_fingerprint_thread,
                         args=(name, national_id, section, department, year, image_path)).start()

    def enroll_fingerprint_thread(self, name, national_id, section, department, year, image_path):
        start_time = time.time()
        while time.time() - start_time < 10:
            fingerprint_id = self.read_fingerprint_id()
            if fingerprint_id is not None:
                # Ensure the data is stored as a dictionary
                self.registered_fingerprints[fingerprint_id] = {
                    "national_id": national_id,
                    "name": name,
                    "section": section,
                    "department": department,
                    "year": year,
                    "image_path": image_path
                }
                self.update_registered_list()
                self.clear_registration_fields()
                self.status_bar.config(text=f"Fingerprint enrolled successfully with ID: {fingerprint_id}")
                self.save_data()  # Save to MongoDB
                self.progress_bar.stop()
                return
            time.sleep(0.1)
        self.status_bar.config(text="Fingerprint enrollment timed out.")
        self.progress_bar.stop()

    def clear_registration_fields(self):
        self.name_entry.delete(0, tk.END)
        self.national_id_entry.delete(0, tk.END)
        self.section_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.image_path = None

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.image_path = file_path
            messagebox.showinfo("Success", "Image uploaded successfully!")

    def delete_fingerprint(self):
        selected = self.registered_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Please select a fingerprint to delete.")
            return

        fingerprint_id = int(self.registered_list.get(selected[0]).split(",")[0].split(":")[1].strip())
        del self.registered_fingerprints[fingerprint_id]
        self.update_registered_list()
        self.status_bar.config(text=f"Fingerprint ID {fingerprint_id} deleted.")
        self.save_data()  # Save to MongoDB

    def clear_fingerprints(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all fingerprints?"):
            self.registered_fingerprints.clear()
            self.update_registered_list()
            self.status_bar.config(text="All fingerprints cleared.")
            self.save_data()  # Save to MongoDB

    def search_fingerprint(self):
        query = self.search_entry.get().strip().lower()
        if not query:
            self.update_registered_list()
            return

        results = []
        for fingerprint_id, data in self.registered_fingerprints.items():
            if (query in str(fingerprint_id).lower() or
                    query in data["name"].lower() or
                    query in data["national_id"].lower() or
                    query in data["section"].lower() or
                    query in data["department"].lower() or
                    query in data["year"].lower()):
                results.append(
                    f"ID: {fingerprint_id}, Name: {data['name']}, National ID: {data['national_id']}, Section: {data['section']}, Department: {data['department']}, Year: {data['year']}")

        self.registered_list.delete(0, tk.END)
        for result in results:
            self.registered_list.insert(tk.END, result)

    def export_data(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "National ID", "Name", "Section", "Department", "Year", "Image Path"])
            for fingerprint_id, data in self.registered_fingerprints.items():
                writer.writerow([fingerprint_id, data["national_id"], data["name"], data["section"], data["department"],
                                 data["year"], data["image_path"]])

        self.status_bar.config(text=f"Data exported to {file_path}")

    def show_help(self):
        messagebox.showinfo("Help",
                            "1. Register a fingerprint: Enter details and click 'Register'.\n"
                            "2. Delete a fingerprint: Select a fingerprint and click 'Delete Selected'.\n"
                            "3. Clear all fingerprints: Click 'Clear All'.\n"
                            "4. Search: Enter a name, ID, or other details in the search bar.\n"
                            "5. Export: Click 'File > Export' to save the list to a CSV file."
                            )

    def update_registered_list(self):
        self.registered_list.delete(0, tk.END)
        for fingerprint_id, data in self.registered_fingerprints.items():
            self.registered_list.insert(tk.END,
                                        f"ID: {fingerprint_id}, Name: {data['name']}, National ID: {data['national_id']}, Section: {data['section']}, Department: {data['department']}, Year: {data['year']}")

    def setup_gui(self):
        self.root.title("Fingerprint Registration System")
        self.root.geometry("1000x700")

        # Load icons
        try:
            self.verified_icon = ImageTk.PhotoImage(Image.open("J:/graduationproject/pythonProject1/verified.png").resize((64, 64)))
            self.unverified_icon = ImageTk.PhotoImage(Image.open("J:/graduationproject/pythonProject1/unverified.jpeg").resize((64, 64)))
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"Image file not found: {e}")
            self.root.quit()

        # Menu Bar
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Export", command=self.export_data)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Help", command=self.show_help)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # Detection Frame
        detection_frame = ttk.LabelFrame(self.root, text="Fingerprint Detection")
        detection_frame.pack(pady=10, padx=10, fill="x")

        self.label = tk.Label(detection_frame, text="Waiting for fingerprint...", font=("Roboto", 18))
        self.label.pack(pady=10)

        self.fingerprint_image_label = tk.Label(detection_frame, image=self.unverified_icon)
        self.fingerprint_image_label.pack(pady=10)

        self.user_image_label = tk.Label(detection_frame)
        self.user_image_label.pack(pady=10)

        # Registration Frame
        registration_frame = ttk.LabelFrame(self.root, text="Register New Fingerprint")
        registration_frame.pack(pady=10, padx=10, fill="x")

        name_label = tk.Label(registration_frame, text="Name:")
        name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(registration_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        national_id_label = tk.Label(registration_frame, text="National ID:")
        national_id_label.grid(row=1, column=0, padx=5, pady=5)
        self.national_id_entry = tk.Entry(registration_frame, width=30)
        self.national_id_entry.grid(row=1, column=1, padx=5, pady=5)

        section_label = tk.Label(registration_frame, text="Section:")
        section_label.grid(row=2, column=0, padx=5, pady=5)
        self.section_entry = tk.Entry(registration_frame, width=30)
        self.section_entry.grid(row=2, column=1, padx=5, pady=5)

        department_label = tk.Label(registration_frame, text="Department:")
        department_label.grid(row=3, column=0, padx=5, pady=5)
        self.department_entry = tk.Entry(registration_frame, width=30)
        self.department_entry.grid(row=3, column=1, padx=5, pady=5)

        year_label = tk.Label(registration_frame, text="Year:")
        year_label.grid(row=4, column=0, padx=5, pady=5)
        self.year_entry = tk.Entry(registration_frame, width=30)
        self.year_entry.grid(row=4, column=1, padx=5, pady=5)

        self.image_path = None
        image_button = ttk.Button(registration_frame, text="Upload Image", command=self.upload_image)
        image_button.grid(row=5, column=0, columnspan=2, pady=5)

        register_button = ttk.Button(registration_frame, text="Register", command=self.register_fingerprint)
        register_button.grid(row=6, column=0, columnspan=2, pady=5)

        # Progress Bar
        self.progress_bar = Progressbar(registration_frame, orient="horizontal", length=200, mode="indeterminate")
        self.progress_bar.grid(row=7, column=0, columnspan=2, pady=5)

        # Search Frame
        search_frame = ttk.LabelFrame(self.root, text="Search Fingerprints")
        search_frame.pack(pady=10, padx=10, fill="x")

        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.pack(side="left", padx=5, pady=5)

        search_button = ttk.Button(search_frame, text="Search", command=self.search_fingerprint)
        search_button.pack(side="left", padx=5, pady=5)

        # Registered Fingerprints Frame
        registered_frame = ttk.LabelFrame(self.root, text="Registered Fingerprints")
        registered_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.registered_list = tk.Listbox(registered_frame, width=100, height=10)
        self.registered_list.pack(pady=10, padx=10, fill="both", expand=True)

        # Buttons Frame
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(pady=10, padx=10, fill="x")

        delete_button = ttk.Button(buttons_frame, text="Delete Selected", command=self.delete_fingerprint)
        delete_button.pack(side="left", padx=5)

        clear_button = ttk.Button(buttons_frame, text="Clear All", command=self.clear_fingerprints)
        clear_button.pack(side="left", padx=5)

        # Status Bar
        self.status_bar = tk.Label(self.root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Start updating the label
        self.root.after(100, self.update_label)


if __name__ == "__main__":
    root = ThemedTk(theme="clam")
    app = FingerprintApp(root)
    root.mainloop()