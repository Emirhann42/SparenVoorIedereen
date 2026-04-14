import tkinter as tk

window = tk.Tk()
window.title("Bankapp - Instellingen")
window.geometry("500x400")
window.configure(bg="#333333")

window.minsize(500, 400)
window.maxsize(700, 500)

titel = tk.Label(
    window,
    text="Instellingen",
    font=("Arial", 18, "bold"),
    bg="#333333",
    fg="white"
)
titel.pack(pady=15)

kaart = tk.Frame(window, bg="white", relief="solid", bd=1)
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

uitloggen_knop = tk.Button(
    kaart,
    text="Uitloggen",
    bg="#0000FF",
    fg="white",
    font=("Arial", 12),
    width=20
)
uitloggen_knop.pack(pady=20)

window.mainloop()