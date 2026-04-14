import tkinter
from tkinter import messagebox

# Opslag voor gebruikers (simpele database)
gebruikers = {}

window = tkinter.Tk()
window.title("Login")
window.geometry('340x440')
window.configure(bg='#333333')

window.maxsize(700, 500)
window.minsize(500, 400)

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in gebruikers and gebruikers[username] == password:
        messagebox.showinfo(title="Login Success", message="Je bent ingelogd!")
    else:
        messagebox.showerror(title="Error", message="Ongeldige login.")

def registreer():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Fout", "Vul alles in!")
    elif username in gebruikers:
        messagebox.showwarning("Fout", "Gebruiker bestaat al!")
    else:
        gebruikers[username] = password
        messagebox.showinfo("Succes", "Registratie gelukt!")

frame = tkinter.Frame(bg='#333333')

# Widgets
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
    font=("Arial", 16), command=registreer)

# Layout
login_label.grid(row=0, column=0, columnspan=2, pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=10)
registreer_button.grid(row=4, column=0, columnspan=2, pady=10)

frame.pack()
window.mainloop()