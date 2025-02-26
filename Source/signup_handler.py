
from flask import Flask, request, jsonify
from tkinter import Toplevel, Label, Entry, Button, Tk, Canvas, PhotoImage
from werkzeug.security import generate_password_hash
from connectionmongo import db 
import signup

coll=db.instructor

def signup_user(user_data):
    try:
        first_name = user_data.get("first_name", "").strip()
        last_name = user_data.get("last_name", "").strip()
        id_number = user_data.get("id_number", "").strip()
        position = user_data.get("position", "").strip()
        email = user_data.get("email", "").strip()
        password = user_data.get("password", "").strip()

        if not all([first_name, last_name, id_number, position, email, password]):
            return {"error": "All fields are required"}, 400

        if coll.find_one({"$or": [{"email": email}, {"id_number": id_number}]}):
            return {"error": "User already exists"}, 400

        hashed_password = generate_password_hash(password)
        user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "id_number": id_number,
            "position": position,
            "email": email,
            "password": hashed_password
        }
        coll.insert_one(user_data)

        return {"message": "User registered successfully"}, 201

    except Exception as e:
        return {"error": str(e)}, 500
