
from flask import Flask, request, jsonify
from tkinter import Toplevel, Label, Entry, Button, Tk, Canvas, PhotoImage
from pathlib import Path
from werkzeug.security import generate_password_hash
from login import open_login_window
from connectionmongo import db
import re

coll=db.instructor



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\TestTrust\Tkinter-Designer-master\Source\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_signup_window(parent):
     # hide home page 
    parent.withdraw() 

    window = Toplevel(parent)
    window.geometry("1250x650")
    window.configure(bg="#FFFFFF")
    window.title("TestTrust")

    def on_close():
        parent.deiconify()
        window.destroy()


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
    canvas.create_text(
        451.0,
        35.0,
        anchor="nw",
        text="Create Account",
        fill="#E86405",
        font=("Inter Bold", 36 * -1)
    )
    
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(457.0, 188.5, image=entry_image_1)
    entry_1 = Entry(window, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_1.place(x=340.0, y=163.0, width=234.0, height=49.0)
    
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(728.0, 189.0, image=entry_image_2)
    entry_2 = Entry(window,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_2.place(x=606.0, y=164.0, width=244.0, height=48.0)
    
    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(728.0, 267.0, image=entry_image_3)
    entry_3 = Entry(window,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_3.place(x=606.0, y=242.0, width=244.0, height=48.0)
    
    entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(457.0, 267.0, image=entry_image_4)
    entry_4 = Entry(window,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_4.place(x=340.0, y=242.0, width=234.0, height=48.0)
    
    entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(595.0, 346.0, image=entry_image_5)
    entry_5 = Entry(window,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_5.place(x=340.0, y=321.0, width=510.0, height=48.0)
    
    entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(595.0, 426.5, image=entry_image_6)
    entry_6 = Entry(window,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, show="*")
    entry_6.place(x=340.0, y=399.0, width=510.0, height=53.0)
    
    canvas.create_text(352.0, 144.0, anchor="nw", text="First Name", fill="#797373", font=("Inter Medium", 14 * -1))
    canvas.create_text(352.0, 223.0, anchor="nw", text="ID Number", fill="#797373", font=("Inter Medium", 14 * -1))
    canvas.create_text(605.0, 223.0, anchor="nw", text="Position", fill="#797373", font=("Inter Medium", 14 * -1))
    canvas.create_text(352.0, 302.0, anchor="nw", text="Email", fill="#797373", font=("Inter Medium", 14 * -1))
    canvas.create_text(352.0, 381.0, anchor="nw", text="Password\n", fill="#797373", font=("Inter Medium", 14 * -1))
    canvas.create_text(605.0, 144.0, anchor="nw", text="Last Name", fill="#797373", font=("Inter Medium", 14 * -1))

    error_label = Label(window, text="", fg="red", font=("Inter", 11), bg="#FFFFFF")
    error_label.place(x=352, y=460)

    entries = [entry_1, entry_2, entry_3, entry_4, entry_5, entry_6]




    def check_entries():
        empty_fields = [i+1 for i, entry in enumerate(entries) if not entry.get().strip()]
    
        if empty_fields:
         error_label.config(text="⚠️ Please fill all fields!")
        else:
         error_label.config(text="")

           
         first_name = entry_1.get().strip()
         last_name = entry_2.get().strip()
         id_number = entry_4.get().strip()
         position = entry_3.get().strip()
         email = entry_5.get().strip()
         password = entry_6.get().strip()
         window.update_idletasks() #refresh the input fileds 
         hashed_password = generate_password_hash(password)

         def is_valid_gmail(email):
           gmail_pattern = r"^[a-zA-Z0-9]+@gmail\.com$"
           return re.match(gmail_pattern, email)
         

         def is_valid_password(password):
           password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
           return re.match(password_pattern, password)
         
       
         user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "id_number": id_number,
            "position": position,
            "email": email,
            "password": hashed_password
        }
         

         
    
         
         
         existing1=coll.find_one({
           "$or": [
            {"email": user_data["email"]},
            {"id_number": user_data["id_number"]}
        ]
})       
          
        if existing1:
           
           existing_email_match = existing1["email"] == user_data["email"]
           existing_id_match = existing1["id_number"] == user_data["id_number"]
           if existing1["email"] == user_data["email"] and existing1["id_number"] ==user_data["id_number"]:
              error_label.config(text="⚠️ Email and ID already exist!")
           elif existing1["email"] == user_data["email"]:
              error_label.config(text="⚠️ Gmail already exists")
           elif  existing1["id_number"] == user_data["id_number"]:
              error_label.config(text="⚠️ ID already exists")
           elif not is_valid_gmail(email):
              error_label.config(text="⚠️ Please enter a valid Gmail address!")
              return
           elif not is_valid_password(password):
              error_label.config(text="⚠️ Password must be at least 8 characters and contain upper, lower, and numbers!")
              return
           elif not id_number.isdigit or len(id_number) != 5:
              error_label.config(text="⚠️ Please enter a valid ID!")
        else:
          error_label.config(text="✅ User registered successfully")  
          coll.insert_one(user_data)

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=check_entries,
        relief="flat"
    )
    button_1.image = button_image_1
    button_1.place(x=352.0, y=489.0, width=488.0, height=50.0)
    
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_login_window(window),
        relief="flat"
    )
    button_2.image = button_image_2
    button_2.place(x=354.0, y=551.0, width=251.0, height=39.0)

    
    canvas.create_rectangle(449.0, 77.0, 728.0, 79.0, fill="#E86405", outline="")

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(1080.0, 404.0, image=image_image_1)
    


    button_image_3 = PhotoImage( file=relative_to_assets("button_3.png"))
    button_3 = Button(
        window,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=on_close,relief="flat"
    )
    button_3.image = button_image_3
    button_3.place(x=17.0, y=26.0, width=209.0, height=62.0)
    
    
    
    
    window.resizable(False, False)
    window.mainloop()


