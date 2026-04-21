import tkinter as tk
from tkinter import messagebox
import sqlite3


class TransactieScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#333333")

        self.controller = controller

        tk.Label(
            self,
            text="Storten / Opnemen",
            font=("Arial", 18, "bold"),
            bg="#333333",
            fg="white"
        ).pack(pady=10)

        self.welkom_label = tk.Label(
            self,
            text="Goedemiddag, Gast",
            font=("Arial", 14),
            bg="white",
            width=30,
            height=2,
            relief="solid"
        )
        self.welkom_label.pack(pady=5)

        self.saldo_var = tk.StringVar(value="€ 0,00")

        tk.Label(
            self,
            textvariable=self.saldo_var,
            font=("Arial", 24, "bold"),
            bg="white",
            width=15,
            height=2,
            relief="solid"
        ).pack(pady=10)

        self.bedrag_invoer = tk.Entry(
            self,
            font=("Arial", 14),
            justify="center",
            width=15
        )
        self.bedrag_invoer.pack(pady=5)

        knoppen_frame = tk.Frame(self, bg="#333333")
        knoppen_frame.pack(pady=10)

        tk.Button(
            knoppen_frame,
            text="Storten",
            width=15,
            height=2,
            bg="#0000FF",
            fg="white",
            command=lambda: self.transactie("storting")
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            knoppen_frame,
            text="Opnemen",
            width=15,
            height=2,
            bg="#0000FF",
            fg="white",
            command=lambda: self.transactie("opname")
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            self,
            text="← Terug",
            command=lambda: controller.show_frame("HomeScreen")
        ).pack(pady=10)

    def format_euro(self, bedrag):
        return f"€ {bedrag:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def update_data(self):
        if self.controller.current_user:
            naam = self.controller.current_user[1]
        else:
            naam = "Gast"

        if self.controller.current_bank:
            saldo = float(self.controller.current_bank[2])
        else:
            saldo = 0

        self.welkom_label.config(text=f"Goedemiddag, {naam}")
        self.saldo_var.set(self.format_euro(saldo))


    def transactie(self, modus):
        invoer = self.bedrag_invoer.get().strip().replace(",", ".")

        try:
            bedrag = float(invoer)
            if bedrag <= 0:
                raise ValueError
        except:
            messagebox.showerror("Fout", "Voer een geldig bedrag in.")
            return

        if not self.controller.current_bank:
            messagebox.showerror("Fout", "Geen rekening gevonden.")
            return

        saldo = float(self.controller.current_bank[2])

        if modus == "opname" and bedrag > saldo:
            messagebox.showerror("Fout", "Onvoldoende saldo.")
            return

        nieuw_saldo = saldo + bedrag if modus == "storting" else saldo - bedrag

        con = sqlite3.connect("database.db")
        cur = con.cursor()

        cur.execute(
            "UPDATE spaarrekening SET saldo = ? WHERE rekening_id = ?",
            (nieuw_saldo, self.controller.current_bank[0])
        )

        con.commit()
        con.close()

        self.controller.current_bank = (
            self.controller.current_bank[0],
            self.controller.current_bank[1],
            nieuw_saldo,
            self.controller.current_bank[3],
            self.controller.current_bank[4]
        )

        self.saldo_var.set(self.format_euro(nieuw_saldo))
        self.bedrag_invoer.delete(0, tk.END)

        messagebox.showinfo(
            "Succes",
            f"{'Gestort' if modus == 'storting' else 'Opgenomen'}: {self.format_euro(bedrag)}"
        )