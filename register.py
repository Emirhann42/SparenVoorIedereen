import tkinter as tk
from tkinter import messagebox
import sqlite3


class RegisterScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#333333")

        self.controller = controller

        tk.Label(
            self,
            text="Register",
            bg="#333333",
            fg="#0000FF",
            font=("Arial", 30)
        ).pack(pady=30)

        form = tk.Frame(self, bg="#333333")
        form.pack()

        tk.Label(form, text="Naam", bg="#333333", fg="white", font=("Arial", 14)).grid(row=0, column=0, pady=5)
        self.naam_entry = tk.Entry(form, font=("Arial", 14))
        self.naam_entry.grid(row=0, column=1, pady=5)

        tk.Label(form, text="Adres", bg="#333333", fg="white", font=("Arial", 14)).grid(row=1, column=0, pady=5)
        self.adres_entry = tk.Entry(form, font=("Arial", 14))
        self.adres_entry.grid(row=1, column=1, pady=5)

        tk.Label(form, text="Email", bg="#333333", fg="white", font=("Arial", 14)).grid(row=2, column=0, pady=5)
        self.email_entry = tk.Entry(form, font=("Arial", 14))
        self.email_entry.grid(row=2, column=1, pady=5)

        tk.Label(form, text="Telefoon", bg="#333333", fg="white", font=("Arial", 14)).grid(row=3, column=0, pady=5)
        self.telefoon_entry = tk.Entry(form, font=("Arial", 14))
        self.telefoon_entry.grid(row=3, column=1, pady=5)

        tk.Label(form, text="Wachtwoord", bg="#333333", fg="white", font=("Arial", 14)).grid(row=4, column=0, pady=5)
        self.wachtwoord_entry = tk.Entry(form, font=("Arial", 14), show="*")
        self.wachtwoord_entry.grid(row=4, column=1, pady=5)

        tk.Button(
            self,
            text="Register",
            bg="#0000FF",
            fg="white",
            font=("Arial", 16),
            width=15,
            command=self.register
        ).pack(pady=20)

        tk.Button(
            self,
            text="← Back to Login",
            bg="#00AA00",
            fg="white",
            font=("Arial", 14),
            width=15,
            command=lambda: controller.show_frame("LoginScreen")
        ).pack()

    def register(self):
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        naam = self.naam_entry.get()
        adres = self.adres_entry.get()
        email = self.email_entry.get()
        telefoon = self.telefoon_entry.get()
        wachtwoord = self.wachtwoord_entry.get()

        if not naam or not email or not wachtwoord:
            messagebox.showerror("Error", "Vul alle verplichte velden in!")
            return

        try:
            cur.execute("""
                INSERT INTO klanten (naam, adres, email, telefoonnummer, wachtwoord)
                VALUES (?, ?, ?, ?, ?)
            """, (naam, adres, email, telefoon, wachtwoord))

            con.commit()
            con.close()

            messagebox.showinfo("Success", "Account aangemaakt!")

            self.controller.show_frame("LoginScreen")

        except Exception as e:
            messagebox.showerror("Error", f"Fout: {e}")
            con.close()