import tkinter as tk


class TransactiesScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#333333")

        self.controller = controller

        # ---------------- TITLE ----------------
        titel = tk.Label(
            self,
            text="Transacties",
            font=("Arial", 18, "bold"),
            bg="#333333",
            fg="white"
        )
        titel.pack(pady=10)

        # ---------------- SEARCH / FILTER ----------------
        boven_frame = tk.Frame(self, bg="#333333")
        boven_frame.pack(pady=10)

        self.zoek_entry = tk.Entry(
            boven_frame,
            width=25,
            font=("Arial", 12)
        )
        self.zoek_entry.insert(0, "Zoek")
        self.zoek_entry.grid(row=0, column=0, padx=5)

        filter_knop = tk.Button(
            boven_frame,
            text="Filter",
            width=10,
            bg="#0000FF",
            fg="white",
            activebackground="#0000CC"
        )
        filter_knop.grid(row=0, column=1, padx=5)

        # ---------------- LIST FRAME ----------------
        self.lijst_frame = tk.Frame(self, bg="white", relief="solid", bd=1)
        self.lijst_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # voorbeeld data
        self.transacties = [
            ("Boodschappen", "€ -45.20"),
            ("Salaris", "€ +1200"),
            ("Netflix", "€ -13.99"),
            ("Tankstation", "€ -60.00")
        ]

        self.toon_transacties()

        # ---------------- BACK BUTTON ----------------
        terug = tk.Button(
            self,
            text="← Terug",
            command=lambda: controller.show_frame("HomeScreen")
        )
        terug.pack(pady=10)

    # ---------------- DISPLAY FUNCTION ----------------
    def toon_transacties(self):
        for widget in self.lijst_frame.winfo_children():
            widget.destroy()

        for naam, bedrag in self.transacties:
            rij = tk.Frame(self.lijst_frame, bg="white")
            rij.pack(fill="x", padx=10, pady=8)

            links = tk.Label(
                rij,
                text=naam,
                bg="white",
                font=("Arial", 12),
                anchor="w"
            )
            links.pack(side="left")

            rechts = tk.Label(
                rij,
                text=bedrag,
                bg="white",
                font=("Arial", 12, "bold"),
                anchor="e"
            )
            rechts.pack(side="right")