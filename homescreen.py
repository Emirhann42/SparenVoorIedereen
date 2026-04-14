import tkinter as tk

# ---- "DATABASE" (simulatie) ----
gebruiker_naam = "Alex"   # <-- dit komt zogenaamd uit database
saldo_bedrag = "€ 1.250,00"

# venster maken
window = tk.Tk()
window.title("Bankapp Dashboard")
window.geometry("500x400")
window.configure(bg="#333333")

# min/max grootte
window.minsize(500, 500)
window.maxsize(700, 600)

# titel
titel = tk.Label(
    window,
    text="Home / Dashboard",
    font=("Arial", 18, "bold"),
    bg="#333333",
    fg="white"
)
titel.pack(pady=10)

# welkom tekst (uit "database")
welkom = tk.Label(
    window,
    text=f"Goedemiddag, {gebruiker_naam}",
    font=("Arial", 14),
    bg="white",
    width=30,
    height=2,
    relief="solid"
)
welkom.pack(pady=5)

# saldo (uit "database")
saldo = tk.Label(
    window,
    text=saldo_bedrag,
    font=("Arial", 24, "bold"),
    bg="white",
    width=15,
    height=2,
    relief="solid"
)
saldo.pack(pady=10)

# frame voor knoppen
knoppen_frame = tk.Frame(window, bg="#333333")
knoppen_frame.pack(pady=10)

# knop functie
def maak_knop(tekst):
    return tk.Button(
        knoppen_frame,
        text=tekst,
        width=15,
        height=2,
        bg="#0000FF",
        fg="white",
        activebackground="#0000CC"
    )

# knoppen
maak_knop("Transacties").grid(row=0, column=0, padx=5, pady=5)
maak_knop("Overboeken").grid(row=0, column=1, padx=5, pady=5)
maak_knop("Rente").grid(row=1, column=0, padx=5, pady=5)
maak_knop("Instellingen").grid(row=1, column=1, padx=5, pady=5)

# titel recente transacties
recente_titel = tk.Label(
    window,
    text="Recente transacties",
    font=("Arial", 13, "bold"),
    bg="#333333",
    fg="white"
)
recente_titel.pack(pady=10)

# frame transacties
transacties_frame = tk.Frame(window, bg="white", relief="solid", bd=1)
transacties_frame.pack(padx=20, pady=5, fill="both")

# puntjes (placeholder)
for i in range(4):
    tk.Label(
        transacties_frame,
        text="...",
        anchor="w",
        bg="white",
        font=("Arial", 12)
    ).pack(fill="x", padx=10, pady=5)

# app starten
window.mainloop()