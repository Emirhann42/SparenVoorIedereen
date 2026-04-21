import tkinter as tk

class SettingsScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#333333")

        self.controller = controller

        titel = tk.Label(
            self,
            text="Instellingen",
            font=("Arial", 18, "bold"),
            bg="#333333",
            fg="white"
        )
        titel.pack(pady=15)

        kaart = tk.Frame(self, bg="white", relief="solid", bd=1)
        kaart.pack(padx=40, pady=10, fill="both")

        def maak_optie(tekst):
            rij = tk.Frame(kaart, bg="white")
            rij.pack(fill="x", padx=10, pady=5)

            label = tk.Label(
                rij,
                text=tekst,
                font=("Arial", 12),
                bg="white",
                anchor="w"
            )
            label.pack(side="left", pady=8)

            pijl = tk.Label(
                rij,
                text=">",
                font=("Arial", 14, "bold"),
                bg="white",
                fg="gray"
            )
            pijl.pack(side="right")

            lijn = tk.Frame(kaart, bg="#d9d9d9", height=1)
            lijn.pack(fill="x", padx=10)

        maak_optie("Profiel")
        maak_optie("Wachtwoord Wijzigen")
        maak_optie("Twee-factor Authenticatie")
        maak_optie("Notificaties")

        # 🔥 LOGOUT BUTTON (now works)
        uitloggen_knop = tk.Button(
            kaart,
            text="Uitloggen",
            bg="#0000FF",
            fg="white",
            font=("Arial", 12),
            width=20,
            command=lambda: controller.show_frame("LoginScreen")
        )
        uitloggen_knop.pack(pady=20)

        # 🔙 Back button (optional but useful)
        terug_knop = tk.Button(
            self,
            text="← Terug",
            command=lambda: controller.show_frame("HomeScreen")
        )
        terug_knop.pack(pady=10)