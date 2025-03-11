import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk, ImageDraw  # For handling images and creating masks
import cv2  # For creating black circles
import numpy as np  # For working with image arrays

class AboutUsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("About Us")
        self.root.geometry("1270x650")
        self.root.configure(bg="#FFFFFF")

        # Navigation Bar
        self.nav_bar = tk.Frame(root, bg="#D9D9D9", height=50)
        self.nav_bar.pack(fill="x")

        # Back Button
        self.back_button = tk.Button(self.nav_bar, text="< Back", fg="#EB5E28", bg="#D9D9D9", bd=0, font=("Arial", 12))
        self.back_button.pack(side="left", padx=10)

        # Logo in the Middle
        try:
            logo_image = Image.open("D:/graduation-project/application/TestTrust/images/Logo.png") 
            logo_image = logo_image.resize((40, 40), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            self.logo_label = tk.Label(self.nav_bar, image=self.logo_photo, bg="#D9D9D9")
            self.logo_label.image = self.logo_photo  # Keep a reference to avoid garbage collection
            self.logo_label.pack(side="left", expand=True)
        except Exception as e:
            print(f"Error loading logo: {e}")
            # Fallback: Use a placeholder text if the logo fails to load
            self.logo_label = tk.Label(self.nav_bar, text="TestTrust", fg="#EB5E28", bg="#D9D9D9", font=("Arial", 12))
            self.logo_label.pack(side="left", expand=True)

        # Clickable Circle on the Right
        self.circle_button = tk.Button(self.nav_bar, text="⚪", fg="black", bg="#D9D9D9", bd=0, font=("Arial", 20))
        self.circle_button.pack(side="right", padx=10)

        # About Us Content
        self.about_frame = tk.Frame(root, bg="#FFFFFF")
        self.about_frame.pack(fill="both", expand=True, pady=20)

        # Grey Box for Header with Black Border
        self.header_box = tk.Frame(
            self.about_frame, 
            bg="#D9D9D9", 
            padx=20, 
            pady=10,
            highlightbackground="#000000",  # Black border color
            highlightthickness=2  # Border thickness
        )
        self.header_box.pack(pady=10, anchor="w", padx=200)  # Align to the left with padding

        # Header inside the grey box
        self.header = tk.Label(self.header_box, text="Test - Trust team", font=("Arial", 15, "bold"), bg="#D9D9D9", fg="#EB5E28")
        self.header.pack(side="left")

        # Orange Triangles (Left and Right)
        try:
            # Left Triangles
            left_triangles_image = Image.open("D:/graduation-project/application/TestTrust/images/Aboutus1.png") 
            left_triangles_image = left_triangles_image.resize((150, 550), Image.LANCZOS)
            self.left_triangles_photo = ImageTk.PhotoImage(left_triangles_image)
            self.left_triangles_label = tk.Label(self.about_frame, image=self.left_triangles_photo, bg="#FFFFFF")
            self.left_triangles_label.image = self.left_triangles_photo
            self.left_triangles_label.place(x=0, y=0, relheight=1.0)  # Place the image on the left side

            # Right Triangles
            right_triangles_image = Image.open("D:/graduation-project/application/TestTrust/images/Aboutus2.png") 
            right_triangles_image = right_triangles_image.resize((150, 550), Image.LANCZOS)
            self.right_triangles_photo = ImageTk.PhotoImage(right_triangles_image)
            self.right_triangles_label = tk.Label(self.about_frame, image=self.right_triangles_photo, bg="#FFFFFF")
            self.right_triangles_label.image = self.right_triangles_photo
            self.right_triangles_label.place(relx=1.0, y=0, anchor="ne", relheight=1.0)  # Place the image on the right side
        except Exception as e:
            print(f"Error loading triangle images: {e}")

        # Description
        self.description = tk.Label(self.about_frame, text="NCTU Information Technology Networking/SoftWare Track", font=("Arial", 20), bg="#FFFFFF", fg="#EB5E28")
        self.description.pack(pady=10)

        # Six Clickable Circles
        self.circles_frame = tk.Frame(self.about_frame, bg="#FFFFFF")
        self.circles_frame.pack(pady=10)

        # Sample data for the circles (name, year, department, LinkedIn URL, email, photo path)
        self.team_members = [
            {"name": "Abdelrahman Sherif Ahmed Bastawy", "year": "4th Year", "department": "ICT/Networking", "linkedin": "https://www.linkedin.com/in/abdelrhman-sherif-541282243/", "email": "boudyshrief.ahmed@gmail.com", "photo": "D:/graduation-project/application/TestTrust/images/person1.Jpg"},
            {"name": "Person 2", "year": "3rd Year", "department": "Mechatronics", "linkedin": "https://linkedin.com/person2", "email": "person2@example.com", "photo": "D:/graduation-project/application/TestTrust/images/person2.Jpg"},
            {"name": "Person 3", "year": "4th Year", "department": "Autotronics", "linkedin": "https://linkedin.com/person3", "email": "person3@example.com", "photo": "D:/graduation-project/application/TestTrust/images/person3.Jpg"},
            {"name": "Person 4", "year": "1st Year", "department": "Renewal Energy", "linkedin": "https://linkedin.com/person4", "email": "person4@example.com", "photo": "D:/graduation-project/application/TestTrust/images/person4.Jpg"},
            {"name": "Person 5", "year": "2nd Year", "department": "ICT", "linkedin": "https://linkedin.com/person5", "email": "person5@example.com", "photo": "D:/graduation-project/application/TestTrust/images/person5.Jpg"},
            {"name": "Person 6", "year": "3rd Year", "department": "Mechatronics", "linkedin": "https://linkedin.com/person6", "email": "person6@example.com", "photo": "D:/graduation-project/application/TestTrust/images/person6.Jpg"},
        ]

        # Create circles for each team member
        for i, member in enumerate(self.team_members):
            try:
                # Load the photo and resize it
                photo_image = Image.open(member["photo"])
                photo_image = photo_image.resize((200, 200), Image.LANCZOS)

                # Create a black circle background using OpenCV
                black_circle = np.zeros((210, 210, 3), dtype=np.uint8)  # Slightly larger to create a border
                cv2.circle(black_circle, (80, 80), 75, (0, 0, 0), -1)  # Draw a black circle

                # Convert the black circle to a PIL image
                black_circle_pil = Image.fromarray(black_circle)

                # Paste the photo onto the black circle
                black_circle_pil.paste(photo_image, (5, 5))  # Center the photo on the black circle

                # Convert the final image to a PhotoImage
                final_image = ImageTk.PhotoImage(black_circle_pil)

                # Create a label with the final image
                circle = tk.Label(
                    self.circles_frame, 
                    image=final_image, 
                    bg="#FFFFFF", 
                    bd=0
                )
                circle.image = final_image  # Keep a reference to avoid garbage collection
                circle.bind("<Button-1>", lambda e, m=member: self.show_member_info(m))  # Make the label clickable
                circle.grid(row=i//3, column=i%3, padx=20, pady=20)  # Add more spacing between circles
            except Exception as e:
                print(f"Error loading photo for {member['name']}: {e}")
                # Fallback: Use a placeholder circle if the photo fails to load
                circle = tk.Label(
                    self.circles_frame, 
                    text="⚪", 
                    fg="black", 
                    bg="#FFFFFF", 
                    font=("Arial", 20),
                    bd=0
                )
                circle.bind("<Button-1>", lambda e, m=member: self.show_member_info(m))  # Make the label clickable
                circle.grid(row=i//3, column=i%3, padx=20, pady=20)  # Add more spacing between circles

    def show_member_info(self, member):
        """Show a small window with information about the team member."""
        info_window = tk.Toplevel(self.root)
        info_window.title(member["name"])
        info_window.geometry("500x400")  # Adjusted size to fit the image and text
        info_window.configure(bg="#FFFFFF")  # Set background to white
        info_window.resizable(False, False)

        # Load the team member's image
        try:
            photo_image = Image.open(member["photo"])
            photo_image = photo_image.resize((150, 150), Image.LANCZOS)  # Resize the image
            photo = ImageTk.PhotoImage(photo_image)
            photo_label = tk.Label(info_window, image=photo, bg="#FFFFFF")
            photo_label.image = photo  # Keep a reference to avoid garbage collection
            photo_label.pack(pady=10)  # Add padding at the top
        except Exception as e:
            print(f"Error loading photo for {member['name']}: {e}")
            # Fallback: Use a placeholder if the image fails to load
            photo_label = tk.Label(info_window, text="No Image", bg="#FFFFFF", fg="#EB5E28", font=("Arial", 12))
            photo_label.pack(pady=10)

        # Member Information
        tk.Label(
            info_window, 
            text=f"Name: {member['name']}", 
            font=("Arial", 12), 
            bg="#FFFFFF", 
            fg="#EB5E28"  # Set text color to #EB5E28
        ).pack(pady=5)

        tk.Label(
            info_window, 
            text=f"Year: {member['year']}", 
            font=("Arial", 12), 
            bg="#FFFFFF", 
            fg="#EB5E28"  # Set text color to #EB5E28
        ).pack(pady=5)

        tk.Label(
            info_window, 
            text=f"Department: {member['department']}", 
            font=("Arial", 12), 
            bg="#FFFFFF", 
            fg="#EB5E28"  # Set text color to #EB5E28
        ).pack(pady=5)

        # LinkedIn URL (clickable)
        linkedin_label = tk.Label(
            info_window, 
            text=f"LinkedIn: {member['linkedin']}", 
            font=("Arial", 12), 
            bg="#FFFFFF", 
            fg="#EB5E28",  # Set text color to #EB5E28
            cursor="hand2"  # Change cursor to a hand when hovering over the link
        )
        linkedin_label.pack(pady=5)
        linkedin_label.bind("<Button-1>", lambda e: webbrowser.open(member["linkedin"]))  # Open the LinkedIn URL when clicked

        tk.Label(
            info_window, 
            text=f"Email: {member['email']}", 
            font=("Arial", 12), 
            bg="#FFFFFF", 
            fg="#EB5E28"  # Set text color to #EB5E28
        ).pack(pady=5)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AboutUsApp(root)
    root.mainloop()