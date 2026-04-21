import tkinter as tk
import datetime


class RenteScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#333333")

        self.controller = controller

        # ---- DATA ----
        self.rente_voor_spaarder = 0.018

        # ---- TITLE ----
        titel = tk.Label(
            self,
            text="Renteoverzicht",
            font=("Arial", 18, "bold"),
            bg="#333333",
            fg="white"
        )
        titel.pack(pady=10)

        # ---- FRAME ----
        frame = tk.Frame(self, bg="white", relief="solid", bd=1)
        frame.pack(padx=20, pady=10)

        self.canvas = tk.Canvas(
            frame,
            width=280,
            height=140,
            bg="white",
            highlightthickness=0
        )
        self.canvas.pack(pady=5)

        self.invoer = tk.Entry(frame, font=("Arial", 12), justify="center")
        self.invoer.insert(0, "100")
        self.invoer.pack(pady=5)

        knop = tk.Button(
            frame,
            text="Bereken",
            bg="#0000FF",
            fg="white",
            width=15,
            command=self.bereken
        )
        knop.pack(pady=10)

        terug = tk.Button(
            frame,
            text="← Terug",
            command=lambda: controller.show_frame("HomeScreen")
        )
        terug.pack(pady=10)

        # first draw
        self.teken_grafiek(self.canvas, self.maak_data(1000, 100))

    # ---------------- LOGIC ----------------

    def rentepercentage_berekenen(self, saldo):
        if saldo <= 0:
            return 0
        elif saldo <= 10000:
            return self.rente_voor_spaarder - 0.0025
        elif saldo <= 25000:
            return self.rente_voor_spaarder
        elif saldo <= 50000:
            return self.rente_voor_spaarder - 0.0015
        else:
            return self.rente_voor_spaarder - 0.005

    def schrikkel_jaar(self):
        jaar = datetime.datetime.now().year
        return (jaar % 4 == 0 and jaar % 100 != 0) or (jaar % 400 == 0)

    def rente_berekenen(self, saldo):
        dagen = 366 if self.schrikkel_jaar() else 365
        return (self.rentepercentage_berekenen(saldo) / dagen) * saldo

    def maak_data(self, start_saldo, per_maand):
        data = []
        saldo = start_saldo

        for i in range(6):
            saldo += per_maand
            saldo += self.rente_berekenen(saldo) * 30
            data.append(round(saldo, 2))

        return data

    def teken_grafiek(self, canvas, data):
        canvas.delete("all")

        links = 20
        onder = 120

        for y in [30, 55, 80, 105]:
            canvas.create_line(20, y, 260, y, fill="#cccccc", dash=(3, 3))

        min_waarde = min(data)
        max_waarde = max(data)

        if max_waarde == min_waarde:
            max_waarde += 1

        punten = []
        stap_x = 48

        for i, waarde in enumerate(data):
            x = links + i * stap_x
            y = onder - ((waarde - min_waarde) / (max_waarde - min_waarde)) * 70
            punten.append((x, y))

        vlak = []
        for x, y in punten:
            vlak.extend([x, y])

        vlak.extend([punten[-1][0], onder, punten[0][0], onder])
        canvas.create_polygon(vlak, fill="#d9d9d9", outline="")

        for i in range(len(punten) - 1):
            canvas.create_line(
                punten[i][0], punten[i][1],
                punten[i + 1][0], punten[i + 1][1],
                fill="#666666",
                width=2
            )

        for x, y in punten:
            canvas.create_oval(x-4, y-4, x+4, y+4,
                                fill="white", outline="#666666", width=2)

    def bereken(self):
        try:
            bedrag = float(self.invoer.get())
        except:
            bedrag = 100

        data = self.maak_data(1000, bedrag)
        self.teken_grafiek(self.canvas, data)