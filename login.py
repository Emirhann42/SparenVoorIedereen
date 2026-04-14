import tkinter
from tkinter import messagebox
import sqlite3

def login():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    mail = username_entry.get()
    password = password_entry.get()
    cur.execute("SELECT * FROM klanten WHERE email == ? AND wachtwoord == ?", (mail, password))
    result = cur.fetchone()
    if result:
        print("Logged in")
    else:
        print("Failed")

def register():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    name = naam_entry.get()
    adress = adres_entry.get()
    email = email_entry.get()
    telefoon = telefoon_entry.get()
    password = wachtwoord_entry.get()
    cur.execute("INSERT INTO klanten (naam, adres, email, telefoonnummer, wachtwoord) VALUES (?,?,?,?,?)", (name,adress,email,telefoon,password))
    con.commit()


window = tkinter.Tk()
window.title("Login")
window.geometry('340x440')
window.configure(bg='#333333')

window.maxsize(700, 500)
window.minsize(500, 400)

frame = tkinter.Frame(bg='#333333')

login_label = tkinter.Label(
    frame, text="Login", bg='#333333', fg="#0000FF", font=("Arial", 30))

username_label = tkinter.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))

username_entry = tkinter.Entry(frame, font=("Arial", 16))

password_label = tkinter.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))

password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))

login_button = tkinter.Button(
    frame, text="Login", bg="#0000FF", fg="#FFFFFF",
    font=("Arial", 16), command=login)

registreer_button = tkinter.Button(
    frame, text="Registreer", bg="#00AA00", fg="#FFFFFF",
    font=("Arial", 16))

login_label.grid(row=0, column=0, columnspan=2, pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=10)
registreer_button.grid(row=4, column=0, columnspan=2, pady=10)

frame.pack()
window.mainloop()