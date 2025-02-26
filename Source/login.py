from pathlib import Path
from tkinter import Toplevel, Label, Entry, Button, Canvas, PhotoImage
from login_handler import login_user  

def relative_to_assets(path: str) -> Path:
    ASSETS_PATH = Path(r"G:\TestTrust\Tkinter-Designer-master\Source\assets\frame3")
    return ASSETS_PATH / Path(path)

def open_login_window(parent):
    parent.withdraw()
    
    window = Toplevel(parent)
    window.geometry("1250x650")
    window.configure(bg="#FFFFFF")
    window.title("TestTrust")

    def on_close():
        parent.deiconify()
        window.destroy()
    


    def submit_login():
        username = entry_1.get().strip()  
        password = entry_2.get().strip()  
        response, status_code = login_user(username, password)

        if status_code == 200:
           print(response["message"]) 
           window.destroy() 
           #open_home_window(parent)
        else:
           print(response["error"])  

    
    # Canvas
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=650,
        width=1250,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    canvas.create_rectangle(0, 0, 1280, 650, fill="#FFFFFF", outline="")

    canvas.create_text(419.0, 90.0, anchor="nw", text="Log in ", fill="#EB5E28", font=("AbrilFatface Regular", 40 * -1))
    
    
    window.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    canvas.create_image(632.5, 238.5, image=window.entry_image_1)
    entry_1 = Entry(window, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_1.place(x=425.0, y=213.0, width=415.0, height=49.0)
    canvas.create_text(419.0, 183.0, anchor="nw", text="Username", fill="#403D39", font=("Inter", 20 * -1))

    window.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    canvas.create_image(632.5, 340.5, image=window.entry_image_2)
    entry_2 = Entry(window,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, show="*")
    entry_2.place(x=425.0, y=315.0, width=415.0, height=49.0)
    canvas.create_text(419.0, 282.0, anchor="nw", text="Password", fill="#403D39", font=("Inter", 20 * -1))

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(window, image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("Login clicked"), relief="flat")
    button_1.image = button_image_1
    button_1.place(x=703.0, y=376.0, width=143.0, height=24.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(window, image=button_image_2, borderwidth=0, highlightthickness=0, command=submit_login, relief="flat")
    button_2.image = button_image_2
    button_2.place(x=529.0, y=412.0, width=213.0, height=38.0)

   
    canvas.create_rectangle(418.0, 151.0, 565.0, 152.0, fill="#EB5E28", outline="")

    
    window.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(162.0, 363.0, image=window.image_image_1)
    
    window.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    canvas.create_image(1090.0, 411.0, image=window.image_image_2)
    
    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(window,  image=button_image_3, borderwidth=0, highlightthickness=0, command=on_close, relief="flat")
    button_3.image = button_image_3
    button_3.place(x=75.0, y=27.0, width=201.0, height=44.0)
    
    window.resizable(False, False)
    window.mainloop()