import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk  # For handling images

class AddExamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Test Trust")
        self.root.geometry("1250x650")
        self.root.configure(bg="#FFFFFF")

        # Load triangle images
        self.triangle1 = ImageTk.PhotoImage(Image.open("D:/graduation-project/application/TestTrust/images/exam1.1.png").resize((200, 150), Image.LANCZOS))
        self.triangle2 = ImageTk.PhotoImage(Image.open("D:/graduation-project/application/TestTrust/images/exam1.2.png").resize((200, 150), Image.LANCZOS))
        self.triangle3 = ImageTk.PhotoImage(Image.open("D:/graduation-project/application/TestTrust/images/exam1.3.png").resize((100, 200), Image.LANCZOS))
        self.triangle4 = ImageTk.PhotoImage(Image.open("D:/graduation-project/application/TestTrust/images/exam1.4.png").resize((200, 200), Image.LANCZOS))

        # Place triangle images
        self.place_triangles()

        # Navigation Bar
        nav_bar = tk.Frame(root, bg="#D9D9D9", height=50, border=2)
        nav_bar.pack(fill="x")

        # Back Button
        back_button = tk.Button(nav_bar, text="< Back", fg="#EB5E28", bg="#D9D9D9", bd=0, font=("Arial", 12))
        back_button.pack(side="left", padx=10)

        # Logo in the Middle
        try:
            logo_image = Image.open("D:/graduation-project/application/TestTrust/images/Logo.png")
            logo_image = logo_image.resize((40, 40), Image.LANCZOS)
            logo_photo = ImageTk.PhotoImage(logo_image)
            logo_label = tk.Label(nav_bar, image=logo_photo, bg="#D9D9D9")
            logo_label.image = logo_photo  # Keep a reference to avoid garbage collection
            logo_label.pack(side="left", expand=True)
        except Exception as e:
            print(f"Error loading logo: {e}")
            # Fallback: Use a placeholder text if the logo fails to load
            logo_label = tk.Label(nav_bar, text="TestTrust", fg="#EB5E28", bg="#D9D9D9", font=("Arial", 12))
            logo_label.pack(side="left", expand=True)

        # Clickable Circle on the Right
        circle_button = tk.Button(nav_bar, text="⚪", fg="black", bg="#D9D9D9", bd=0, font=("Arial", 20))
        circle_button.pack(side="right", padx=10)

        # Header
        header = tk.Label(root, text="Hey Again! Time For A New Exam", font=("Arial", 16, "bold"), bg="#FFFFFF", fg="#EB5E28")
        header.pack(pady=10)

        # Frame for input fields
        input_frame = tk.Frame(root, bg="#FFFFFF", width=850, height=200)
        input_frame.pack(pady=10)
        input_frame.pack_propagate(False)

        # Custom Style for Entry Fields and Comboboxes
        style = ttk.Style()
        style.configure("Custom.TEntry",
                        bordercolor="#CCCCCC",  # Light grey border
                        lightcolor="#CCCCCC",
                        darkcolor="#CCCCCC",
                        padding=5,  # Space between text and border
                        relief="solid",  # Border style
                        font=("Arial", 12))  # Font for the entry fields

        style.configure("Custom.TCombobox",
                        bordercolor="#CCCCCC",  # Light grey border
                        lightcolor="#CCCCCC",
                        darkcolor="#CCCCCC",
                        padding=5,  # Space between text and border
                        relief="solid",  # Border style
                        font=("Arial", 12)),  # Font for the comboboxes

        # Department (Drop-Down)
        tk.Label(input_frame, text="Department", bg="#FFFFFF", fg="#EB5E28", font=("Abril Fatface", 19)).grid(row=0, column=0, padx=0, pady=5)
        self.department_entry = ttk.Combobox(input_frame, values=["ICT", "Mechatronics", "Autotronics", "Renewal Energy"], width=27, style="Custom.TCombobox")
        self.department_entry.grid(row=0, column=1, padx=15, pady=5)

        # Year (Drop-Down)
        tk.Label(input_frame, text="Year", bg="#FFFFFF", fg="#EB5E28", font=("Abril Fatface", 19)).grid(row=1, column=0, padx=0, pady=5)
        self.year_entry = ttk.Combobox(input_frame, values=["1st Year", "2nd Year", "3rd Year", "4th Year"], width=27, style="Custom.TCombobox")
        self.year_entry.grid(row=1, column=1, padx=10, pady=5)

        # Subject
        tk.Label(input_frame, text="Subject", bg="#FFFFFF", fg="#EB5E28", font=("Abril Fatface", 19)).grid(row=2, column=0, padx=0, pady=5)
        self.subject_entry = ttk.Entry(input_frame, width=30, style="Custom.TEntry")
        self.subject_entry.grid(row=2, column=1, padx=10, pady=5)

        # Number of Students
        tk.Label(input_frame, text="No. Of Students", bg="#FFFFFF", fg="#EB5E28", font=("Abril Fatface", 19)).grid(row=3, column=0, padx=0, pady=5)
        self.students_entry = ttk.Entry(input_frame, width=30, style="Custom.TEntry")
        self.students_entry.grid(row=3, column=1, padx=10, pady=5)

        # Exam Date
        tk.Label(input_frame, text="Exam Date", bg="#FFFFFF", fg="#EB5E28", font=("Abril Fatface", 19)).grid(row=4, column=0, padx=0, pady=5)
        self.date_entry = ttk.Entry(input_frame, width=30, style="Custom.TEntry")
        self.date_entry.grid(row=4, column=1, padx=10, pady=5)

        # Duration
        tk.Label(input_frame, text="Duration (in Hours)", bg="#FFFFFF", fg="#EB5E28", font=("Abril Fatface", 19)).grid(row=5, column=0, padx=0, pady=5)
        self.duration_entry = ttk.Entry(input_frame, width=30, style="Custom.TEntry")
        self.duration_entry.grid(row=5, column=1, padx=10, pady=5)

        # Total Marks
        tk.Label(input_frame, text="Total Marks", bg="#FFFFFF", fg="#EB5E28", font=("Abril Fatface", 19)).grid(row=6, column=0, padx=0, pady=5)
        self.marks_entry = ttk.Entry(input_frame, width=30, style="Custom.TEntry")
        self.marks_entry.grid(row=6, column=1, padx=10, pady=5)

        # Number of Exam Questions
        tk.Label(input_frame, text="No. Of Exam Questions", bg="#FFFFFF", fg="#EB5E28", font=("Abril Fatface", 19)).grid(row=7, column=0, padx=0, pady=5)
        self.questions_entry = ttk.Entry(input_frame, width=30, style="Custom.TEntry")
        self.questions_entry.grid(row=7, column=1, padx=10, pady=5)

        # Next Button
        next_button = tk.Button(root, text="Next", command=self.save_exam, bg="#EB5E28", fg="white", font=("Inter", 15), width=10)
        next_button.pack(pady=30)

        # Bind window resize event
        self.root.bind("<Configure>", self.on_window_resize)

    def place_triangles(self):
        # Place triangle images at specific positions
        self.triangle1_label = tk.Label(self.root, image=self.triangle1, bg="#FFFFFF")
        self.triangle2_label = tk.Label(self.root, image=self.triangle2, bg="#FFFFFF")
        self.triangle3_label = tk.Label(self.root, image=self.triangle3, bg="#FFFFFF")
        self.triangle4_label = tk.Label(self.root, image=self.triangle4, bg="#FFFFFF")

        # Update triangle positions
        self.update_triangle_positions()

    def update_triangle_positions(self):
        # Get the current window size
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        # Define positions as percentages of the window size
        self.triangle1_label.place(x=0, y=int(0.05 * window_height))  # Top-left corner
        self.triangle2_label.place(x=window_width - 200, y=int(0.05 * window_height))  # Top-right corner
        self.triangle3_label.place(x=0, y=int(0.7 * window_height))  # Bottom-left corner
        self.triangle4_label.place(x=window_width - 200, y=int(0.7 * window_height))  # Bottom-right corner

    def on_window_resize(self, event):
        # Update triangle positions when the window is resized
        self.update_triangle_positions()

    def save_exam(self):
        # Retrieve data from entries
        department = self.department_entry.get()
        year = self.year_entry.get()
        subject = self.subject_entry.get()
        students = self.students_entry.get()
        date = self.date_entry.get()
        duration = self.duration_entry.get()
        marks = self.marks_entry.get()
        questions = self.questions_entry.get()

        # Validate inputs
        if not all([department, year, subject, students, date, duration, marks, questions]):
            messagebox.showwarning("Input Error", "Please fill all fields!")
            return

        # Save or process the data (you can add database logic here)
        exam_details = {
            "Department": department,
            "Year": year,
            "Subject": subject,
            "No. Of Students": students,
            "Exam Date": date,
            "Duration": duration,
            "Total Marks": marks,
            "No. Of Questions": questions
        }

        # Display success message
        messagebox.showinfo("Success", "Exam details saved successfully!")
        print(exam_details)  # Replace with database logic

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AddExamApp(root)
    root.mainloop()