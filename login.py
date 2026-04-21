import tkinter as tk
from tkinter import messagebox
import sqlite3


class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#333333")

        self.controller = controller

        # ---------------- UI ----------------
        login_label = tk.Label(
            self, text="Login",
            bg='#333333', fg="#0000FF",
            font=("Arial", 30)
        )
        login_label.pack(pady=30)

        self.username_entry = tk.Entry(self, font=("Arial", 16))
        self.username_entry.pack(pady=10)

        self.password_entry = tk.Entry(self, show="*", font=("Arial", 16))
        self.password_entry.pack(pady=10)

        login_button = tk.Button(
            self,
            text="Login",
            bg="#0000FF",
            fg="white",
            font=("Arial", 16),
            command=self.login
        )
        login_button.pack(pady=10)

        register_button = tk.Button(
            self,
            text="Registreer",
            bg="#00AA00",
            fg="white",
            font=("Arial", 16),
            command=lambda: controller.show_frame("RegisterScreen")
        )
        register_button.pack(pady=10)

    # ---------------- LOGIN LOGIC ----------------
    def login(self):
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        email = self.username_entry.get()
        wachtwoord = self.password_entry.get()

        cur.execute(
            "SELECT * FROM klanten WHERE email = ? AND wachtwoord = ?",
            (email, wachtwoord)
        )

        result = cur.fetchone()
        con.close()

        if result:
            messagebox.showinfo("Success", "Logged in!")

            # 🔥 GO TO HOME SCREEN
            self.controller.show_frame("HomeScreen")

        else:
            messagebox.showerror("Error", "Wrong email or password")