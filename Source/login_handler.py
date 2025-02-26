from flask import Flask, request, jsonify
from tkinter import Toplevel, Label, Entry, Button, Tk, Canvas, PhotoImage
from connectionmongo import db 
import login

coll=db.instructor

def login_user(username, password):
    try:
        user = coll.find_one({"$or": [{"email": username}, {"password": password}]})

        if not user:
            return {"error": "User does not exist"}, 404  
        if not coll(user["password"], password):
            return {"error": "Incorrect password"}, 401  

        return {"message": "Login successful"}, 200  
    except Exception as e:
        return {"error": str(e)}, 500  
