from tkinter import Toplevel, Label, Entry, Button, Tk, Canvas, PhotoImage
from pathlib import Path
from dashboard import open_dashboard

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\TestTrust\Tkinter-Designer-master\build\assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)






window=Tk()
window.geometry("1150x650")
window.configure(bg="#FFFFFF")



canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=650,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
canvas.place(x=0, y=0)
    
canvas.create_rectangle(
        0.0, 0.0, 1280.0, 650.0,
        fill="#F5F1EB", outline=""
    )
canvas.create_rectangle(
        394.0, 55.0, 885.0, 594.0,
        fill="#D9D9D9", outline=""
    )
    
canvas.create_text(
        419.0, 90.0, anchor="nw", text="Log in ",
        fill="#EB5E28", font=("AbrilFatface Regular", 40 * -1)
    )
    
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(632.5, 267.5, image=entry_image_1)
    
entry_1 = Entry(
        bd=0, bg="#CCC5B9", fg="#000716", highlightthickness=0
    )
entry_1.place(
        x=423.0, y=235.0, width=419.0, height=63.0
    )
    
canvas.create_text(
        419.0, 183.0, anchor="nw", text="Username",
        fill="#403D39", font=("Abel Regular", 32 * -1)
    )
    
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(632.5, 388.5, image=entry_image_2)
    
entry_2 = Entry(
        bd=0, bg="#CCC5B9", fg="#000716", highlightthickness=0
    )
entry_2.place(
        x=423.0, y=356.0, width=419.0, height=63.0
    )
    
canvas.create_text(
        419.0, 313.0, anchor="nw", text="Password",
        fill="#403D39", font=("Abel Regular", 32 * -1)
    )
    
button_image_1 = PhotoImage(file=relative_to_assets("button_lost.png"))
button_1 = Button(
        image=button_image_1, borderwidth=0, highlightthickness=0,
        command=lambda: print("button_1 clicked"), relief="flat"
    )
button_1.place(
        x=723.0, y=432.0, width=143.0, height=24.0
    )
    
button_image_2 = PhotoImage(file=relative_to_assets("button_login.png"))
button_2 = Button(
        image=button_image_2, borderwidth=0, highlightthickness=0,
        command=lambda: print("button_create clicked"), relief="flat"
    )
button_2.place(
        x=419.0, y=467.0, width=423.0, height=47.0
    )
    
button_image_3 = PhotoImage(file=relative_to_assets("button_create.png"))
button_3 = Button(
        image=button_image_3, borderwidth=0, highlightthickness=0,
        command=lambda: print("button_3 clicked"), relief="flat"
    )
button_3.place(
        x=419.0, y=531.0, width=202.0, height=43.0
    )
    
button_image_4 = PhotoImage(file=relative_to_assets("button_back.png"))
button_4 = Button(
        image=button_image_4, borderwidth=0, highlightthickness=0,
        command=lambda: print("button_4 clicked"), relief="flat"
    )
button_4.place(
        x=41.0, y=18.0, width=137.0, height=37.0
    )
    
window.mainloop()
