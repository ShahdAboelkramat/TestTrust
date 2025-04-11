import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Configuration parameters for sizing
CONFIG = {
    "window_size": {"width": 1250, "height": 650},
    "nav_bar": {"height": 50, "back_button_padx": 10, "circle_button_padx": 10},
    "title": {"padx": 30, "pady": 5, "font_size": 13},
    "search": {"ipady": 0, "binocular_padx": 0, "font_size": 10},
    "list_container": {"padx": 10, "pady": 0, "height": 200, "width": 800},
    "exam_entry": {"padx": 10, "pady": 5, "spacer_width": 420, "font_size": 10},
    "bottom_section": {
        "pady_top": 20, 
        "pady_bottom": 20, 
        "padx_between": 10,
        "container_padx": 10,
        "container_pady": 20
    },
    "left_rect": {"padx": 10, "pady": 10, "width": 250, "height": 350},
    "right_rect": {"padx": 10, "pady": 10, "width": 350, "height": 350},
    "info_frames": {"pady": 5, "label_padx": 10},
    "qa_section": {"pady_top": 20, "entry_padx": 10, "entry_width": 30},
    "buttons": {"view_details_padx": 5, "trash_padx": 5, "edit_padx": 15, "done_padx": 20, "done_pady_top": 10}
}

def manage_exam():
    # Create main window
    root = tk.Tk()
    root.title("View Upcoming Exams")
    root.geometry(f"{CONFIG['window_size']['width']}x{CONFIG['window_size']['height']}")
    root.configure(bg="#EB5E28")  
    
    # Navigation Bar
    nav_bar = tk.Frame(root, bg="#D9D9D9", height=CONFIG['nav_bar']['height'], borderwidth=2, relief="solid")
    nav_bar.pack(fill="x", pady=(0, 20))
    
    # Back Button
    back_button = tk.Button(nav_bar, text="< Back", fg="#EB5E28", bg="#D9D9D9", 
                          bd=0, font=("Arial", 12))
    back_button.pack(side="left", padx=CONFIG['nav_bar']['back_button_padx'])
    
    # Logo in the Middle
    try:
        logo_image = Image.open("D:/graduation-project/application/TestTrust/images/Logo.png")
        logo_image = logo_image.resize((40, 40), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(nav_bar, image=logo_photo, bg="#D9D9D9")
        logo_label.image = logo_photo
        logo_label.pack(side="left", expand=True)
    except Exception as e:
        print(f"Error loading logo: {e}")
        logo_label = tk.Label(nav_bar, text="TestTrust", fg="#EB5E28", bg="#D9D9D9", font=("Arial", 12))
        logo_label.pack(side="left", expand=True)
    
    # Clickable Circle on the Right
    circle_button = tk.Button(nav_bar, text="⚪", fg="black", bg="#D9D9D9", 
                            bd=0, font=("Arial", 20))
    circle_button.pack(side="right", padx=CONFIG['nav_bar']['circle_button_padx'])
    
    # Main content frame
    content_frame = tk.Frame(root, bg="#EB5E28")
    content_frame.pack(fill="both", expand=True, padx=20, pady=10)
    
    # Header section with filter
    header_frame = tk.Frame(content_frame, bg="#EB5E28")
    header_frame.pack(fill="x")
    
    # Orange header with black border
    title_frame = tk.Frame(header_frame, bg="#EB5E28", bd=2, relief="solid")
    title_frame.pack(side="left", padx=(0, 20))
    
    title_label = tk.Label(title_frame, text="View Upcoming Exams", 
                          font=("Arial", CONFIG['title']['font_size'], "bold"), 
                          bg="#D9D9D9", fg="#EB5E28", 
                          padx=CONFIG['title']['padx'], pady=CONFIG['title']['pady'])
    title_label.pack()
    
    # Search filter with binocular icon
    search_frame = tk.Frame(header_frame, bg="#EB5E28")
    search_frame.pack(side="right", fill="x", expand=False)
    
    search_entry = tk.Entry(search_frame, font=("Arial", CONFIG['search']['font_size']), 
                          bd=1, relief="solid", bg="white", fg="grey")
    search_entry.insert(0, "provide a filter")
    search_entry.pack(side="left", fill="x", expand=True, ipady=CONFIG['search']['ipady'])
    
    # Binocular icon (using text as placeholder)
    binocular_icon = tk.Label(search_frame, text="🔍", font=("Arial", 14), 
                            bg="#EB5E28")
    binocular_icon.pack(side="left", padx=(CONFIG['search']['binocular_padx'], 0))
    
    # Exams list container (light grey rounded rectangle)
    list_container = tk.Frame(content_frame, bg="#E0E0E0", bd=2, 
                            relief="solid", 
                            padx=CONFIG['list_container']['padx'], 
                            pady=CONFIG['list_container']['pady'], 
                            width=CONFIG['list_container']['width'],
                            height=CONFIG['list_container']['height'])
    list_container.pack_propagate(False)
    list_container.pack(fill="both", expand=True, pady=(0, 0))
    
    # Canvas and scrollbar for the exams list
    canvas = tk.Canvas(list_container, bg="#E0E0E0", highlightthickness=2)
    scrollbar = ttk.Scrollbar(list_container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#E0E0E0")
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Exam data
    exams = [
        ["CCNA", "4TH", "25/4/2025", "30 ST", "DR.mohamed", "30 Q/A", "IT"],
        ["Big Data", "4TH", "28/4/2025", "20 ST", "DR.Eman", "15 Q/A", "IT"],
        ["Network Admin", "4TH", "28/4/2025", "25 ST", "DR.Amani", "20 Q/A", "IT"],
        ["Database", "3RD", "30/4/2025", "25 ST", "DR.Samir", "25 Q/A", "IT"],
        ["Security", "4TH", "2/5/2025", "30 ST", "DR.Noha", "30 Q/A", "IT"]
    ]
    
    # Add exam entries (grey rounded rectangles)
    for exam in exams:
        entry_frame = tk.Frame(scrollable_frame, bg="#4b4b4b", bd=0, 
                             highlightbackground="#606060", highlightthickness=1,
                             padx=CONFIG['exam_entry']['padx'], 
                             pady=CONFIG['exam_entry']['pady'])
        entry_frame.pack(fill="x", padx=CONFIG['list_container']['padx'], pady=5)
        
        # Exam details (white text)
        for i, detail in enumerate(exam):
            detail_label = tk.Label(entry_frame, text=detail, 
                                   font=("Arial", CONFIG['exam_entry']['font_size']), 
                                   bg="#4b4b4b", fg="white")
            detail_label.pack(side="left", padx=(0 if i == 0 else 15), expand=True)
        
        # Spacer to push buttons to the right
        spacer = tk.Frame(entry_frame, bg="#4b4b4b", 
                         width=CONFIG['exam_entry']['spacer_width'])
        spacer.pack(side="left", expand=True, fill="x")
        
        # View Details button
        view_button = tk.Button(entry_frame, text="View Details", 
                              font=("Arial", CONFIG['exam_entry']['font_size'], "bold"), 
                              bg="#4b4b4b", fg="black", bd=0)
        view_button.pack(side="left", padx=CONFIG['buttons']['view_details_padx'])
        
        # Trash icon (using text as placeholder)
        trash_icon = tk.Button(entry_frame, text="🗑️", font=("Arial", 15), 
                             bg="#4b4b4b", fg="black", bd=0)
        trash_icon.pack(side="left", padx=CONFIG['buttons']['trash_padx'])
    
    # Bottom section - create a container rectangle first
    bottom_container = tk.Frame(content_frame, bg="#D9D9D9", bd=2, relief="solid",
                               padx=CONFIG['bottom_section']['container_padx'],
                               pady=CONFIG['bottom_section']['container_pady'])
    bottom_container.pack(fill="x", 
                        pady=(CONFIG['bottom_section']['pady_top'], 
                             CONFIG['bottom_section']['pady_bottom']))
    
    # Frame to hold the two rectangles inside the container
    bottom_frame = tk.Frame(bottom_container, bg="#D9D9D9")
    bottom_frame.pack(fill="both", expand=True)
    
    # Left rectangle (now inside the container) - Black background
    left_rect = tk.Frame(bottom_frame, bg='#4b4b4b', bd=0,
                        width=CONFIG['left_rect']['width'],
                        height=CONFIG['left_rect']['height'])
    left_rect.pack_propagate(False)
    left_rect.pack(side="left", fill="both", expand=False,
                 padx=(0, CONFIG['bottom_section']['padx_between']))
    
    # Content frame for left rectangle
    left_content = tk.Frame(left_rect, bg='#4b4b4b')
    left_content.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Exam info in left rectangle (only showing Subject, Year, Date)
    exam_info_left = [
        ("Exam Subject:", "CCNA"),
        ("Year:", "4TH"),
        ("Exam Date:", "25/4/2025")
    ]
    
    for i, (label_text, value_text) in enumerate(exam_info_left):
        info_frame = tk.Frame(left_content, bg='#4b4b4b')
        info_frame.pack(fill="x", pady=5)
        
        label = tk.Label(info_frame, text=label_text, font=("Arial", 10, "bold"), 
                        bg='#4b4b4b', fg='white')
        label.pack(side="left")
        
        value = tk.Label(info_frame, text=value_text, font=("Arial", 10), 
                        bg='#4b4b4b', fg='white')
        value.pack(side="left", padx=5)
    
    # Edit button at bottom of left rectangle
    edit_button = tk.Button(left_content, text="Edit", 
                         font=("Arial", 10, "bold"), 
                         bg="#EB5E28", fg="white", bd=0, 
                         padx=20, pady=5)
    edit_button.pack(side="bottom", pady=10)
    
    # Right rectangle (now inside the container) - Black background
    right_rect = tk.Frame(bottom_frame, bg='#4b4b4b', bd=0,
                         width=CONFIG['right_rect']['width'],
                         height=CONFIG['right_rect']['height'])
    right_rect.pack_propagate(False)
    right_rect.pack(side="right", fill="both", expand=True,
                  padx=(CONFIG['bottom_section']['padx_between'], 0))
    
    # Content frame for right rectangle
    right_content = tk.Frame(right_rect, bg='#4b4b4b')
    right_content.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Split right rectangle into left and right sections
    right_left = tk.Frame(right_content, bg='#4b4b4b')
    right_left.pack(side="left", fill="both", expand=True, padx=5, pady=5)
    
    right_right = tk.Frame(right_content, bg='#4b4b4b')
    right_right.pack(side="right", fill="both", expand=True, padx=5, pady=5)
    
    # Left side of right rectangle - Entry fields
    entry_fields = [
        ("Subject:", 20),
        ("Department:", 20),
        ("Year:", 20),
        ("Duration:", 20),
        ("Mark:", 20),
        ("Date:", 20)
    ]
    
    for field, width in entry_fields:
        field_frame = tk.Frame(right_left, bg='#4b4b4b')
        field_frame.pack(fill="x", pady=2)
        
        label = tk.Label(field_frame, text=field, font=("Arial", 10), 
                       bg='#4b4b4b', fg='white')
        label.pack(side="left")
        
        entry = tk.Entry(field_frame, font=("Arial", 10), 
                        bd=1, relief="solid", width=width)
        entry.pack(side="right")
    
    # Add Done button to bottom of left section in right rectangle
    done_button = tk.Button(right_left, text="Done", 
                          font=("Arial", 10, "bold"), 
                          bg="#EB5E28", fg="white", bd=0, 
                          padx=20, pady=5)
    done_button.pack(side="bottom", pady=10)
    
    # Right side of right rectangle - Filter search bars
    filter_frame = tk.Frame(right_right, bg='#4b4b4b')
    filter_frame.pack(fill="x", pady=5)
    
    filter1_label = tk.Label(filter_frame, text="Filter by Q No:", 
                           font=("Arial", 10), bg='#4b4b4b', fg='white')
    filter1_label.pack(side="left")
    
    filter1_entry = tk.Entry(filter_frame, font=("Arial", 10), 
                           bd=1, relief="solid", width=15)
    filter1_entry.pack(side="left", padx=5)
    
    filter2_label = tk.Label(filter_frame, text="Filter by Q Type:", 
                           font=("Arial", 10), bg='#4b4b4b', fg='white')
    filter2_label.pack(side="left")
    
    filter2_entry = tk.Entry(filter_frame, font=("Arial", 10), 
                           bd=1, relief="solid", width=15)
    filter2_entry.pack(side="left", padx=5)
    
    # Question and Answer entries below filters
    qa_frame = tk.Frame(right_right, bg='#4b4b4b')
    qa_frame.pack(fill="x", pady=10)
    
    question_label = tk.Label(qa_frame, text="Question:", 
                            font=("Arial", 10), bg='#4b4b4b', fg='white')
    question_label.pack(anchor="w")
    
    question_entry = tk.Text(qa_frame, font=("Arial", 10), 
                           bd=1, relief="solid", height=4, width=40)
    question_entry.pack(fill="x")
    
    answer_label = tk.Label(qa_frame, text="Answer:", 
                          font=("Arial", 10), bg='#4b4b4b', fg='white')
    answer_label.pack(anchor="w", pady=(10, 0))
    
    answer_entry = tk.Text(qa_frame, font=("Arial", 10), 
                         bd=1, relief="solid", height=4, width=40)
    answer_entry.pack(fill="x")
    
    root.mainloop()

if __name__ == "__main__":
    manage_exam()