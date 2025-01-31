from tkinter import Toplevel, Label, Entry, Button, Tk, Canvas, PhotoImage
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\TestTrust\Tkinter-Designer-master\Source\assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_login_window(parent):
     # hide home page 
    parent.withdraw() 

    window = Toplevel(parent)
    window.geometry("1150x650")
    window.configure(bg="#FFFFFF")
    window.title("TestTrust")

# reload the home page when close the login page 
    def on_close():
        parent.deiconify()  
        window.destroy()

    canvas = Canvas(
        window, bg="#FFFFFF", height=650, width=1150,
        bd=0, highlightthickness=0, relief="ridge"
    )
    canvas.place(x=0, y=0)

    canvas.create_rectangle(0.0, 0.0, 1280.0, 650.0, fill="#F5F1EB", outline="")
    canvas.create_rectangle(394.0, 55.0, 885.0, 594.0, fill="#D9D9D9", outline="")

    canvas.create_text(419.0, 90.0, anchor="nw", text="Log in", fill="#EB5E28", font=("AbrilFatface Regular", 40 * -1))

    entry_1 = Entry(window, bd=0, bg="#CCC5B9", fg="#000716", highlightthickness=0)
    entry_1.place(x=423.0, y=235.0, width=419.0, height=63.0)
    canvas.create_text(419.0, 183.0, anchor="nw", text="Username", fill="#403D39", font=("Abel Regular", 32 * -1))

    entry_2 = Entry(window, bd=0, bg="#CCC5B9", fg="#000716", highlightthickness=0, show="*")
    entry_2.place(x=423.0, y=356.0, width=419.0, height=63.0)
    canvas.create_text(419.0, 313.0, anchor="nw", text="Password", fill="#403D39", font=("Abel Regular", 32 * -1))

    # lost password button
    button_image_1 = PhotoImage(file=relative_to_assets("button_lost.png"))
    button_1 = Button(
        window, image=button_image_1, borderwidth=0, highlightthickness=0,
        command=lambda: print("Lost Password Clicked"), relief="flat"
    )
    button_1.image = button_image_1
    button_1.place(x=723.0, y=432.0, width=143.0, height=24.0)

    # login button
    button_image_2 = PhotoImage(file=relative_to_assets("button_login.png"))
    button_2 = Button(
        window, image=button_image_2, borderwidth=0, highlightthickness=0,
        command=lambda: print("Login Clicked"), relief="flat"
    )
    button_2.image = button_image_2
    button_2.place(x=419.0, y=467.0, width=423.0, height=47.0)

    # Create Account button
    button_image_3 = PhotoImage(file=relative_to_assets("button_create.png"))
    button_3 = Button(
        window, image=button_image_3, borderwidth=0, highlightthickness=0,
        command=lambda: print("Create Account Clicked"), relief="flat"
    )
    button_3.image = button_image_3
    button_3.place(x=419.0, y=531.0, width=202.0, height=43.0)

    # back button
    button_image_4 = PhotoImage(file=relative_to_assets("button_back.png"))
    button_4 = Button(
        window, image=button_image_4, borderwidth=0, highlightthickness=0,
        command= on_close, relief="flat"
    )
    button_4.image = button_image_4
    button_4.place(x=41.0, y=18.0, width=137.0, height=37.0)

    window.resizable(False, False)
    window.mainloop()
