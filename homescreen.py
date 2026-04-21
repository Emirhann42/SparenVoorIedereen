import tkinter as tk


class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#333333")

        self.controller = controller

        # ---- "DATABASE" (simulatie) ----
        gebruiker_naam = "Alex"
        saldo_bedrag = "€ 1.250,00"

        # titel
        titel = tk.Label(
            self,
            text="Home / Dashboard",
            font=("Arial", 18, "bold"),
            bg="#333333",
            fg="white"
        )
        titel.pack(pady=10)

        # welkom tekst
        welkom = tk.Label(
            self,
            text=f"Goedemiddag, {gebruiker_naam}",
            font=("Arial", 14),
            bg="white",
            width=30,
            height=2,
            relief="solid"
        )
        welkom.pack(pady=5)

        # saldo
        saldo = tk.Label(
            self,
            text=saldo_bedrag,
            font=("Arial", 24, "bold"),
            bg="white",
            width=15,
            height=2,
            relief="solid"
        )
        saldo.pack(pady=10)

        # frame voor knoppen
        knoppen_frame = tk.Frame(self, bg="#333333")
        knoppen_frame.pack(pady=10)

        # knop functie (NOW WITH ACTION)
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

        # knoppen
        maak_knop("Transacties").grid(row=0, column=0, padx=5, pady=5)
        maak_knop("Overboeken").grid(row=0, column=1, padx=5, pady=5)
        maak_knop("Rente").grid(row=1, column=0, padx=5, pady=5)

        # 🔥 THIS ONE WORKS NOW
        maak_knop(
            "Instellingen",
            command=lambda: controller.show_frame("SettingsScreen")
        ).grid(row=1, column=1, padx=5, pady=5)

        # titel recente transacties
        recente_titel = tk.Label(
            self,
            text="Recente transacties",
            font=("Arial", 13, "bold"),
            bg="#333333",
            fg="white"
        )
        recente_titel.pack(pady=10)

        # frame transacties
        transacties_frame = tk.Frame(self, bg="white", relief="solid", bd=1)
        transacties_frame.pack(padx=20, pady=5, fill="both")

        # placeholder transacties
        for i in range(4):
            tk.Label(
                transacties_frame,
                text="...",
                anchor="w",
                bg="white",
                font=("Arial", 12)
            ).pack(fill="x", padx=10, pady=5)