import tkinter as tk
import datetime

date = datetime.datetime.now()
rente_voor_spaarder = 0.018

def rentepercentage_berekenen(saldo):
    if saldo <= 0:
        return 0
    elif saldo <= 10000:
        return rente_voor_spaarder - 0.0025
    elif saldo <= 25000:
        return rente_voor_spaarder
    elif saldo <= 50000:
        return rente_voor_spaarder - 0.0015
    else:
        return rente_voor_spaarder - 0.005

def schrikkel_jaar():
    jaar = date.year
    return (jaar % 4 == 0 and jaar % 100 != 0) or (jaar % 400 == 0)

def rente_berekenen(saldo):
    dagen = 366 if schrikkel_jaar() else 365
    return (rentepercentage_berekenen(saldo) / dagen) * saldo

def maak_data(start_saldo, per_maand):
    data = []
    saldo = start_saldo

    for i in range(6):
        saldo += per_maand
        saldo += rente_berekenen(saldo) * 30
        data.append(round(saldo, 2))

    return data

def teken_grafiek(canvas, data):
    canvas.delete("all")

    breedte = 280
    hoogte = 140
    links = 20
    onder = 120

    # hulplijnen
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

    # grijs vlak onder grafiek
    vlak = []
    for x, y in punten:
        vlak.extend([x, y])

    vlak.extend([punten[-1][0], onder, punten[0][0], onder])
    canvas.create_polygon(vlak, fill="#d9d9d9", outline="")

    # lijn
    for i in range(len(punten) - 1):
        canvas.create_line(
            punten[i][0], punten[i][1],
            punten[i + 1][0], punten[i + 1][1],
            fill="#666666",
            width=2
        )

    # puntjes
    for x, y in punten:
        canvas.create_oval(x-4, y-4, x+4, y+4, fill="white", outline="#666666", width=2)

def bereken():
    bedrag = float(invoer.get())
    data = maak_data(1000, bedrag)
    teken_grafiek(canvas, data)

window = tk.Tk()
window.title("Renteoverzicht")
window.geometry("500x400")
window.configure(bg="#333333")
window.minsize(500, 400)
window.maxsize(700, 500)

titel = tk.Label(
    window,
    text="Renteoverzicht",
    font=("Arial", 18, "bold"),
    bg="#333333",
    fg="white"
)
titel.pack(pady=10)

frame = tk.Frame(window, bg="white", relief="solid", bd=1)
frame.pack(padx=20, pady=10)

rente_label = tk.Label(
    frame,
    text="Huidige rente: 1.5%",
    font=("Arial", 16, "bold"),
    bg="white"
)
rente_label.pack(pady=10)

canvas = tk.Canvas(
    frame,
    width=280,
    height=140,
    bg="white",
    highlightthickness=0
)
canvas.pack(pady=5)

vraag = tk.Label(
    frame,
    text="Wat als ik €100 p/m spaar?",
    font=("Arial", 12),
    bg="white"
)
vraag.pack(pady=5)

invoer = tk.Entry(frame, font=("Arial", 12), justify="center")
invoer.insert(0, "100")
invoer.pack(pady=5)

knop = tk.Button(
    frame,
    text="Bereken",
    bg="#0000FF",
    fg="white",
    width=15,
    command=bereken
)
knop.pack(pady=10)

teken_grafiek(canvas, maak_data(1000, 100))

window.mainloop()