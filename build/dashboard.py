from tkinter import Toplevel, Label, Entry, Button

def open_dashboard(parent):
    dashboard_window = Toplevel()
    dashboard_window.geometry("1150x650")
    dashboard_window.configure(bg="#F5F1EB")
    dashboard_window.title("Dashboard")

    Label(dashboard_window, text="Welcome to the Dashboard!", font=("Arial", 24)).pack(pady=50)

    def go_back_to_main():
        dashboard_window.destroy()
        parent.deiconify()

    back_button = Button(dashboard_window, text="Back to Main", font=("Arial", 18), command=go_back_to_main)
    back_button.pack(pady=20)

    dashboard_window.mainloop()
