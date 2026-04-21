import tkinter as tk
import sqlite3

class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#333333")

        self.controller = controller

        tk.Label(
            self,
            text="Home / Dashboard",
            font=("Arial", 18, "bold"),
            bg="#333333",
            fg="black"
        ).pack(pady=10)

        self.welkom_label = tk.Label(
            self,
            text="Goedemiddag, Gast",
            font=("Arial", 14),
            bg="black",
            fg="white",
            width=30,
            height=2,
            relief="solid"
        )
        self.welkom_label.pack(pady=5)

        self.saldo_label = tk.Label(
            self,
            text="??",
            font=("Arial", 24, "bold"),
            bg="black",
            fg="white",
            width=15,
            height=2,
            relief="solid"
        )
        self.saldo_label.pack(pady=10)

        knoppen_frame = tk.Frame(self, bg="#333333")
        knoppen_frame.pack(pady=10)

        def maak_knop(tekst, command=None):
            return tk.Button(
                knoppen_frame,
                text=tekst,
                width=15,
                height=2,
                bg="#0000FF",
                fg="white",
                activebackground="#0000CC",
                command=command
            )


        maak_knop(
            "Transacties",
            command=lambda: controller.show_frame("GeschidenisScreen")
        ).grid(row=0, column=0, padx=5, pady=5)

        maak_knop(
            "Overboeken",
            command=lambda: controller.show_frame("TransactieScreen")
        ).grid(row=0, column=1, padx=5, pady=5)

        maak_knop(
            "Rente",
            command=lambda: controller.show_frame("RenteScreen")
        ).grid(row=1, column=0, padx=5, pady=5)

        maak_knop(
            "Instellingen",
            command=lambda: controller.show_frame("SettingsScreen")
        ).grid(row=1, column=1, padx=5, pady=5)


        tk.Label(
            self,
            text="Recente transacties",
            font=("Arial", 13, "bold"),
            bg="#333333",
            fg="white"
        ).pack(pady=10)

        transacties_frame = tk.Frame(self, bg="white", relief="solid", bd=1)
        transacties_frame.pack(padx=20, pady=5, fill="both")


       # def transacties():
        #    con = sqlite3.connect("database.db")
        #    cur = con.cursor()
        #    cur.execute("SELECT * FROM rekening WHERE klantid = " + )
    def update_data(self):

        if self.controller.current_user:
            naam = self.controller.current_user[1]
        else:
            naam = "Gast"

        if self.controller.current_bank:
            saldo = self.controller.current_bank[2]
        else:
            saldo = 0

        self.welkom_label.config(text=f"Goedemiddag, {naam}")
        self.saldo_label.config(text=f"€ {saldo}")