import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # For handling images

class ExamQuestionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Test Trust")
        self.root.geometry("1270x650")
        self.root.configure(bg="#FFFFFF")

        # Load circle images
        try:
            self.circle_left = ImageTk.PhotoImage(Image.open("D:/graduation-project/application/TestTrust/images/circle_left.png").resize((200, 400), Image.LANCZOS))
            self.circle_right = ImageTk.PhotoImage(Image.open("D:/graduation-project/application/TestTrust/images/circle_right.png").resize((200, 400), Image.LANCZOS))
        except Exception as e:
            print(f"Error loading images: {e}")
            # Fallback: Use placeholder text if images fail to load
            self.circle_left = None
            self.circle_right = None

        # Place circle images
        self.place_circles()

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
        header = tk.Label(root, text="Thanks For The Previous Informations, Now Let's Create The Exam :)", font=("Arial", 16, "bold"), bg="#FFFFFF", fg="#EB5E28")
        header.pack(pady=20)

        # Main Frame for Input Fields
        main_frame = tk.Frame(root, bg="#FFFFFF")
        main_frame.pack(fill="both", expand=True, padx=200, pady=10)  # Add padding to avoid overlapping with images

        # Question Type Label
        tk.Label(main_frame, text="Question Type?", bg="#FFFFFF", fg="#EB5E28", font=("Abril Fatface", 19)).pack(pady=10)

        # Question Type Dropdown (Small Combo Box)
        self.question_type = ttk.Combobox(main_frame, values=["MCQ", "Written", "True or False", "Matching"], width=20, font=("Arial", 12))
        self.question_type.configure(style="White.TCombobox")  # Set background to white
        self.question_type.pack(pady=5)
        self.question_type.bind("<<ComboboxSelected>>", self.update_question_format)

        # Custom style for Combobox to set background to white
        style = ttk.Style()
        style.configure("White.TCombobox", background="#FFFFFF", fieldbackground="#FFFFFF", foreground="black")

        # Enter Your Question Label
        tk.Label(main_frame, text="Enter your Question No. 1:", bg="#FFFFFF", fg="#EB5E28", font=("Abril Fatface", 19)).pack(pady=10, padx=100, anchor="w")

        # Rounded Rectangle for Question Entry (Using a Text Widget)
        self.question_entry = tk.Text(main_frame, height=3, width=75, font=("Arial", 12), bd=2, relief="groove", bg="#FFFFFF")
        self.question_entry.pack(pady=10)

        # Correction Option
        correction_frame = tk.Frame(main_frame, bg="#FFFFFF")
        correction_frame.pack(pady=10)

        tk.Label(correction_frame, text="Would you like us to do the correction for you?", bg="#FFFFFF", fg="#EB5E28", font=("Abril Fatface", 19)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.correction_var = tk.StringVar(value="No")
        self.correction_yes = ttk.Radiobutton(correction_frame, text="Yes", variable=self.correction_var, value="Yes", command=self.toggle_answer_field, style="White.TRadiobutton")
        self.correction_yes.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.correction_no = ttk.Radiobutton(correction_frame, text="No", variable=self.correction_var, value="No", command=self.toggle_answer_field, style="White.TRadiobutton")
        self.correction_no.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        # Custom style for Radiobutton to set background to white
        style.configure("White.TRadiobutton", background="#FFFFFF", foreground="black")

        # Answer Field (Dynamic based on question type)
        self.answer_frame = ttk.Frame(main_frame, style="White.TFrame")
        self.answer_frame.pack(pady=10)

        # Custom style for Frame to set background to white
        style.configure("White.TFrame", background="#FFFFFF")

        # Next Button
        next_button = tk.Button(root, text="Next", command=self.submit_form, bg="#EB5E28", fg="white", font=("Inter", 15), width=10)
        next_button.pack(pady=30)

        # Initialize answer widgets
        self.answer_widgets = []
        self.toggle_answer_field()

        # Bind window resize event to update circle positions
        self.root.bind("<Configure>", self.on_window_resize)

    def place_circles(self):
        """Place circle images at specific positions."""
        if self.circle_left and self.circle_right:
            self.circle_left_label = tk.Label(self.root, image=self.circle_left, bg="#FFFFFF")
            self.circle_right_label = tk.Label(self.root, image=self.circle_right, bg="#FFFFFF")

            # Place circles on the far left and far right
            self.circle_left_label.place(x=0, y=150)  # Far left
            self.circle_right_label.place(x=1070, y=150)  # Far right (1270 - 200 = 1070)
        else:
            print("Circle images not loaded. Using placeholder text.")
            tk.Label(self.root, text="Left Circle", bg="#FFFFFF", fg="#EB5E28", font=("Arial", 12)).place(x=0, y=150)
            tk.Label(self.root, text="Right Circle", bg="#FFFFFF", fg="#EB5E28", font=("Arial", 12)).place(x=1070, y=150)

    def on_window_resize(self, event):
        """Update circle positions when the window is resized."""
        self.update_circle_positions()

    def update_circle_positions(self):
        """Update circle positions based on window size."""
        if self.circle_left and self.circle_right:
            self.circle_left_label.place(x=0, y=100)  # Far left
            self.circle_right_label.place(x=self.root.winfo_width() - 200, y=150)  # Far right

    def update_question_format(self, event):
        """Update the answer entry based on the selected question type."""
        selected_type = self.question_type.get()
        self.clear_answer_widgets()  # Clear all previous answer widgets

        if selected_type == "MCQ":
            self.create_mcq_answer_widgets()
        elif selected_type == "True or False":
            self.create_true_false_answer_widgets()
        elif selected_type == "Written":
            self.create_written_answer_widgets()
        elif selected_type == "Matching":
            self.create_matching_answer_widgets()

    def clear_answer_widgets(self):
        """Clear all answer widgets in the answer_frame."""
        for widget in self.answer_frame.winfo_children():
            widget.destroy()
        self.answer_widgets = []

    def create_mcq_answer_widgets(self):
        """Create 4 entry fields for MCQ answers."""
        labels = ["A)", "B)", "C)", "D)"]
        for i, label in enumerate(labels):
            ttk.Label(self.answer_frame, text=label, font=("Abril Fatface", 14), background="#FFFFFF").grid(row=i, column=0, padx=5, pady=5, sticky="w")
            entry = ttk.Entry(self.answer_frame, width=30, font=("Arial", 12), style="White.TEntry")
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            self.answer_widgets.append(entry)

        # Custom style for Entry to set background to white
        style = ttk.Style()
        style.configure("White.TEntry", background="#FFFFFF", fieldbackground="#FFFFFF", foreground="black")

    def create_true_false_answer_widgets(self):
        """Create radio buttons for True or False answers."""
        self.true_false_var = tk.StringVar(value="")  # No default selection
        ttk.Radiobutton(self.answer_frame, text="True", variable=self.true_false_var, value="True", style="White.TRadiobutton").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(self.answer_frame, text="False", variable=self.true_false_var, value="False", style="White.TRadiobutton").grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.answer_widgets.append(self.true_false_var)

    def create_written_answer_widgets(self):
        """Create a single text entry for written answers."""
        entry = ttk.Entry(self.answer_frame, width=75, font=("Arial", 12), style="White.TEntry")
        entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.answer_widgets.append(entry)

    def create_matching_answer_widgets(self):
        """Create two columns for matching pairs."""
        ttk.Label(self.answer_frame, text="Left Column", font=("Abril Fatface", 14), background="#FFFFFF").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(self.answer_frame, text="Right Column", font=("Abril Fatface", 14), background="#FFFFFF").grid(row=0, column=1, padx=5, pady=5, sticky="w")
        for i in range(3):  # Example: 3 pairs
            left_entry = ttk.Entry(self.answer_frame, width=20, font=("Arial", 12), style="White.TEntry")
            left_entry.grid(row=i+1, column=0, padx=5, pady=5, sticky="ew")
            right_entry = ttk.Entry(self.answer_frame, width=20, font=("Arial", 12), style="White.TEntry")
            right_entry.grid(row=i+1, column=1, padx=5, pady=5, sticky="ew")
            self.answer_widgets.extend([left_entry, right_entry])

    def toggle_answer_field(self):
        """Show or hide the answer field based on the correction option."""
        if self.correction_var.get() == "Yes":
            self.answer_frame.pack()
        else:
            self.answer_frame.pack_forget()

    def submit_form(self):
        """Validate and process the form data."""
        question = self.question_entry.get("1.0", tk.END).strip()
        correction = self.correction_var.get()
        selected_type = self.question_type.get()

        if not question:
            messagebox.showwarning("Input Error", "Please enter a question.")
            return

        if correction == "Yes":
            if selected_type == "MCQ":
                answers = [entry.get().strip() for entry in self.answer_widgets]
                if not all(answers):
                    messagebox.showwarning("Input Error", "Please fill all MCQ options.")
                    return
            elif selected_type == "True or False":
                if not self.true_false_var.get():
                    messagebox.showwarning("Input Error", "Please select True or False.")
                    return
            elif selected_type == "Written":
                answer = self.answer_widgets[0].get().strip()
                if not answer:
                    messagebox.showwarning("Input Error", "Please provide the written answer.")
                    return
            elif selected_type == "Matching":
                answers = [entry.get().strip() for entry in self.answer_widgets]
                if not all(answers):
                    messagebox.showwarning("Input Error", "Please fill all matching pairs.")
                    return

        # Process the form data (e.g., save to a file or database)
        print(f"Question: {question}")
        print(f"Correction: {correction}")
        if correction == "Yes":
            print(f"Answer: {answers if selected_type in ['MCQ', 'Matching'] else self.true_false_var.get() if selected_type == 'True or False' else self.answer_widgets[0].get()}")

        messagebox.showinfo("Success", "Question submitted successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExamQuestionApp(root)
    root.mainloop()