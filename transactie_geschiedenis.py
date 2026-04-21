import tkinter as tk


class GeschidenisScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#333333")

        self.controller = controller


        tk.Label(
            self,
            text="Transacties",
            font=("Arial", 18, "bold"),
            bg="#333333",
            fg="white"
        ).pack(pady=10)

        boven_frame = tk.Frame(self, bg="#333333")
        boven_frame.pack(pady=10)

        self.zoek_entry = tk.Entry(
            boven_frame,
            width=25,
            font=("Arial", 12)
        )
        self.zoek_entry.insert(0, "Zoek")
        self.zoek_entry.grid(row=0, column=0, padx=5)

        tk.Button(
            boven_frame,
            text="Filter",
            width=10,
            bg="#0000FF",
            fg="white",
            activebackground="#0000CC",
            command=self.filter_transacties
        ).grid(row=0, column=1, padx=5)


        self.lijst_frame = tk.Frame(self, bg="white", relief="solid", bd=1)
        self.lijst_frame.pack(padx=20, pady=10, fill="both", expand=True)


        self.transacties = [
            ("Boodschappen", "€ -45.20"),
            ("Salaris", "€ +1200"),
            ("Netflix", "€ -13.99"),
            ("Tankstation", "€ -60.00")
        ]

        self.toon_transacties()


        tk.Button(
            self,
            text="← Terug",
            command=lambda: controller.show_frame("HomeScreen")
        ).pack(pady=10)


    def toon_transacties(self, data=None):
        for widget in self.lijst_frame.winfo_children():
            widget.destroy()

        if data is None:
            data = self.transacties

        for naam, bedrag in data:
            rij = tk.Frame(self.lijst_frame, bg="white")
            rij.pack(fill="x", padx=10, pady=8)

            tk.Label(
                rij,
                text=naam,
                bg="white",
                font=("Arial", 12),
                anchor="w"
            ).pack(side="left")

            tk.Label(
                rij,
                text=bedrag,
                bg="white",
                font=("Arial", 12, "bold"),
                anchor="e"
            ).pack(side="right")


    def filter_transacties(self):
        zoekterm = self.zoek_entry.get().lower()

        gefilterd = [
            t for t in self.transacties
            if zoekterm in t[0].lower()
        ]

        self.toon_transacties(gefilterd)