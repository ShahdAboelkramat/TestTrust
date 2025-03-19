import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import calendar
import time

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Test Trust - Dashboard")
        self.root.geometry("1250x650")
        self.root.configure(bg="#EB5E28")  # Light grey background

        # Load images for icons
        self.add_exam_icon = self.load_image("D:/graduation-project/application/TestTrust/images/add_exam.png", (20, 20))
        self.manage_exam_icon = self.load_image("D:/graduation-project/application/TestTrust/images/manage_exam.png", (20, 20))
        self.manage_students_icon = self.load_image("D:/graduation-project/application/TestTrust/images/manage_students.png", (20, 20))
        self.dashboard_image = self.load_image("D:/graduation-project/application/TestTrust/images/dashboard-l.png", (275, 225))
        self.calendar_image = self.load_image("D:/graduation-project/application/TestTrust/images/dashboard.png", (245, 125))

        # Create a custom style for rounded corners
        self.style = ttk.Style()
        self.style.configure("Rounded.TFrame", background="#FFFFFF", borderwidth=2, relief="solid", bordercolor="#D9D9D9")

        # Navigation Bar
        self.create_nav_bar()

        # Main Content Frame
        self.main_frame = tk.Frame(root, bg="#000000")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Left Section: Dashboard Buttons (Reduced Width)
        self.create_left_section(self.main_frame, width=200)  # Increased width for better spacing

        # Middle Section: Exam Status and Upcoming Exams (Increased Width)
        self.create_middle_section(self.main_frame, width=600)  # Adjusted width

        # Right Section: Real-Time Calendar (Reduced Width)
        self.create_right_section(self.main_frame, width=300)

    def load_image(self, path, size):
        """Load and resize an image."""
        try:
            image = Image.open(path)
            image = image.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading image: {e}")
            return None

    def create_nav_bar(self):
        """Create the navigation bar."""
        nav_bar = tk.Frame(self.root, bg="#D9D9D9", height=60)
        nav_bar.pack(fill="x")

        # Back Button
        back_button = tk.Button(nav_bar, text="< Back", fg="#EB5E28", bg="#D9D9D9", bd=0, font=("Arial", 18))
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

    def create_left_section(self, parent, width):
        """Create the left section with dashboard buttons."""
        left_frame = ttk.Frame(parent, style="Rounded.TFrame", width=width)
        left_frame.pack(side="left", fill="y", padx=(10, 5), pady=10)

        # Title: Dashboard
        title_frame = tk.Frame(left_frame, bg="#D9D9D9")
        title_frame.pack(fill="x", pady=(0, 10))  # Added padding at the bottom

        tk.Label(title_frame, text="Dashboard", font=("Arial", 15, "bold"), bg="#D9D9D9", fg="#EB5E28").pack(pady=3)

        # Buttons with Icons
        buttons = [
            ("Add Exam", self.add_exam_icon, self.add_exam),
            ("Manage Exam", self.manage_exam_icon, self.manage_exam),
            ("Manage Students", self.manage_students_icon, self.manage_students),
        ]

        button_frame = tk.Frame(left_frame, bg="#FFFFFF")
        button_frame.pack(fill="both", expand=True, padx=10, pady=15)

        for text, icon, command in buttons:
            button = tk.Button(button_frame, text=text, image=icon, compound="left", bg="#FFFFFF", fg="#333333", font=("Arial", 17), bd=0, command=command, anchor="w")
            button.pack(fill="x", pady=10)

        # Add image beneath buttons
        if self.dashboard_image:
            tk.Label(left_frame, image=self.dashboard_image, bg="#FFFFFF").pack(pady=0)

    def create_middle_section(self, parent, width):
        """Create the middle section with Exam Status and Upcoming Exams."""
        middle_frame = ttk.Frame(parent, style="Rounded.TFrame", width=width)
        middle_frame.pack(side="left", fill="both", expand=True, padx=5, pady=10)

        # Exam Status Section
        exam_status_frame = ttk.Frame(middle_frame, style="Rounded.TFrame")
        exam_status_frame.pack(fill="both", expand=True, pady=(0, 0))  # Added padding at the bottom

        tk.Label(exam_status_frame, text="Exam Status", font=("Arial", 18, "bold"), bg="#D9D9D9", fg="#EB5E28").pack(fill="x", pady=1)

        # Create a Treeview for Exam Status
        exam_status_columns = ("Department", "Year", "Time", "Subject", "Students", "Room")
        exam_status_tree = ttk.Treeview(exam_status_frame, columns=exam_status_columns, show="headings", height=5)
        exam_status_tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Add a scrollbar for the Exam Status Treeview
        exam_status_scrollbar = ttk.Scrollbar(exam_status_frame, orient="vertical", command=exam_status_tree.yview)
        exam_status_scrollbar.pack(side="right", fill="y")
        exam_status_tree.configure(yscrollcommand=exam_status_scrollbar.set)

        # Define column headings
        for col in exam_status_columns:
            exam_status_tree.heading(col, text=col, anchor="center")
            exam_status_tree.column(col, anchor="center", width=100)

        # Add sample data
        exam_status_data = [
            ("IT", "4TH", "I:30:00", "CCNAIV", "30/30", "A201"),
            ("CS", "3RD", "II:45:00", "Python", "25/30", "B101"),
        ]
        for row in exam_status_data:
            exam_status_tree.insert("", "end", values=row)

        # Upcoming Exams Section
        upcoming_exams_frame = ttk.Frame(middle_frame, style="Rounded.TFrame")
        upcoming_exams_frame.pack(fill="both", expand=True, pady=(0, 10))  # Added padding at the bottom

        tk.Label(upcoming_exams_frame, text="Upcoming Exams", font=("Arial", 18, "bold"), bg="#D9D9D9", fg="#EB5E28").pack(fill="x", pady=1)

        # Create a Treeview for Upcoming Exams
        upcoming_exams_columns = ("Department", "Year", "Time", "Subject", "Room", "Date")
        upcoming_exams_tree = ttk.Treeview(upcoming_exams_frame, columns=upcoming_exams_columns, show="headings", height=5)
        upcoming_exams_tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Add a scrollbar for the Upcoming Exams Treeview
        upcoming_exams_scrollbar = ttk.Scrollbar(upcoming_exams_frame, orient="vertical", command=upcoming_exams_tree.yview)
        upcoming_exams_scrollbar.pack(side="right", fill="y")
        upcoming_exams_tree.configure(yscrollcommand=upcoming_exams_scrollbar.set)

        # Define column headings
        for col in upcoming_exams_columns:
            upcoming_exams_tree.heading(col, text=col, anchor="center")
            upcoming_exams_tree.column(col, anchor="center", width=100)

        # Add sample data
        upcoming_exams_data = [
            ("IT", "4TH", "I:30:00", "IOT Security", "A201", "25/3/2025"),
            ("CS", "3RD", "II:45:00", "Data Structures", "B101", "30/3/2025"),
        ]
        for row in upcoming_exams_data:
            upcoming_exams_tree.insert("", "end", values=row)

    def create_right_section(self, parent, width):
        """Create the right section with a real-time calendar."""
        right_frame = ttk.Frame(parent, style="Rounded.TFrame", width=width)
        right_frame.pack(side="right", fill="y", padx=(5, 10), pady=10)

        # Calendar Title
        calendar_title_frame = tk.Frame(right_frame, bg="#D9D9D9")
        calendar_title_frame.pack(fill="x", pady=(0, 10))  # Added padding at the bottom

        tk.Label(calendar_title_frame, text="Reservation Calendar", font=("Arial", 15, "bold"), bg="#D9D9D9", fg="#EB5E28").pack(pady=3)

        # Current Month and Year
        self.current_month_year_label = tk.Label(right_frame, text="", font=("Arial", 14), bg="#FFFFFF", fg="#000000")
        self.current_month_year_label.pack(pady=10)

        # Calendar Navigation Buttons
        button_frame = tk.Frame(right_frame, bg="#FFFFFF")
        button_frame.pack(fill="x", pady=5)

        tk.Button(button_frame, text="<", font=("Arial", 12), bg="#FFFFFF", fg="#EB5E28", bd=0, command=self.prev_month).pack(side="left", padx=5)
        tk.Button(button_frame, text=">", font=("Arial", 12), bg="#FFFFFF", fg="#EB5E28", bd=0, command=self.next_month).pack(side="right", padx=5)

        # Calendar Grid
        self.calendar_frame = tk.Frame(right_frame, bg="#FFFFFF")
        self.calendar_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.current_year = time.localtime().tm_year
        self.current_month = time.localtime().tm_mon
        self.update_calendar_grid()

        # Add another dashboard image below the calendar
        if self.calendar_image:
            image_label = tk.Label(right_frame, image=self.calendar_image, bg="#FFFFFF")
            image_label.pack(pady=0)

    def update_calendar_grid(self):
        """Update the calendar grid with the current month and year."""
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        self.current_month_year_label.config(text=f"{calendar.month_name[self.current_month]} {self.current_year}")

        cal = calendar.monthcalendar(self.current_year, self.current_month)
        for i, week in enumerate(cal):
            for j, day in enumerate(week):
                if day == 0:
                    continue
                day_frame = tk.Frame(self.calendar_frame, bg="#FFFFFF", bd=1, relief="solid")
                day_frame.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

                tk.Label(day_frame, text=str(day), font=("Arial", 10), bg="#FFFFFF", fg="#333333").pack(fill="both", expand=True)

                if day in [25, 30]:  # Highlight reserved dates
                    day_frame.configure(bg="#FFCCCC")

    def prev_month(self):
        """Navigate to the previous month."""
        self.current_month -= 1
        if self.current_month < 1:
            self.current_month = 12
            self.current_year -= 1
        self.update_calendar_grid()

    def next_month(self):
        """Navigate to the next month."""
        self.current_month += 1
        if self.current_month > 12:
            self.current_month = 1
            self.current_year += 1
        self.update_calendar_grid()

    def add_exam(self):
        """Handle Add Exam button click."""
        messagebox.showinfo("Add Exam", "Redirecting to Add Exam page...")

    def manage_exam(self):
        """Handle Manage Exam button click."""
        messagebox.showinfo("Manage Exam", "Redirecting to Manage Exam page...")

    def manage_students(self):
        """Handle Manage Students button click."""
        messagebox.showinfo("Manage Students", "Redirecting to Manage Students page...")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()