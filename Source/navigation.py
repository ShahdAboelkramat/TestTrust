from tkinter import Toplevel

def open_signup_window(parent):
    parent.withdraw()
    signup_window = Toplevel(parent)
    signup_window.geometry("1250x650")
    signup_window.configure(bg="#FFFFFF")
    signup_window.title("TestTrust")

    def on_close():
        parent.deiconify()
        signup_window.destroy()

    signup_window.protocol("WM_DELETE_WINDOW", on_close)
    signup_window.mainloop()

def open_login_window(parent):
    parent.withdraw()
    login_window = Toplevel(parent)
    login_window.geometry("1250x650")
    login_window.configure(bg="#FFFFFF")
    login_window.title("TestTrust")

    def on_close():
        parent.deiconify()
        login_window.destroy()

    login_window.protocol("WM_DELETE_WINDOW", on_close)
    login_window.mainloop()
