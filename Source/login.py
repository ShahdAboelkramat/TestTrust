from pathlib import Path
from tkinter import Toplevel, Label, Entry, Button, Canvas, PhotoImage
from werkzeug.security import check_password_hash
import re 
from connectionmongo import db



coll=db.instructor

def relative_to_assets(path: str) -> Path:
    ASSETS_PATH = Path(r"G:\TestTrust\Application\Source\assets\frame3")
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






    error_label = Label(window, text="", fg="red", font=("Inter", 11), bg="#FFFFFF")
    error_label.place(x=352, y=400)

    entries = [entry_1, entry_2]
   
    def check_entries():
        empty_fields = [i+1 for i, entry in enumerate(entries) if not entry.get().strip()]

        if empty_fields:
         
         error_label.config(text="⚠️ Please fill all fields!")
         return
        else:
        
           
        
         email1 = entry_1.get().strip()
         password1 = entry_2.get().strip()

         window.update_idletasks()  

         def is_valid_gmail(email1):
           gmail_pattern = r"^[a-zA-Z0-9]+@gmail\.com$"
           return re.match(gmail_pattern, email1)
        
         user = coll.find_one({"email":email1})

            
         if not is_valid_gmail(email1):
             error_label.config(text="⚠️ Invalid email!")
         elif  user is None:
             error_label.config(text="⚠️ Email not found!")
         elif not check_password_hash(user["password"], password1):
             error_label.config(text="⚠️ Incorrect password!")   
         else:
            error_label.config(text="welcome")

   
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(window, image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("Login clicked"), relief="flat")
    button_1.image = button_image_1
    button_1.place(x=703.0, y=376.0, width=143.0, height=24.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(window, image=button_image_2, borderwidth=0, highlightthickness=0, command=check_entries, relief="flat")
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