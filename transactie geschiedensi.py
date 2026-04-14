import tkinter as tk

# venster maken
window = tk.Tk()
window.title("Bankapp - Transacties")
window.geometry("500x400")
window.configure(bg="#333333")

# vaste min/max grootte
window.minsize(500, 400)
window.maxsize(700, 500)

# titel
titel = tk.Label(
    window,
    text="Transacties",
    font=("Arial", 18, "bold"),
    bg="#333333",
    fg="white"
)
titel.pack(pady=10)

# zoek en filter frame
boven_frame = tk.Frame(window, bg="#333333")
boven_frame.pack(pady=10)

# zoekvak
zoek_entry = tk.Entry(
    boven_frame,
    width=25,
    font=("Arial", 12)
)
zoek_entry.insert(0, "Zoek")
zoek_entry.grid(row=0, column=0, padx=5)

# filter knop
filter_knop = tk.Button(
    boven_frame,
    text="Filter",
    width=10,
    bg="#0000FF",
    fg="white",
    activebackground="#0000CC"
)
filter_knop.grid(row=0, column=1, padx=5)

# frame voor transactielijst
lijst_frame = tk.Frame(window, bg="white", relief="solid", bd=1)
lijst_frame.pack(padx=20, pady=10, fill="both", expand=True)

# voorbeeld transacties
transacties = [
    ("...", "€ ..."),
    ("...", "€ ..."),
    ("...", "€ ..."),
    ("...", "€ ...")
]

# transacties tonen
for naam, bedrag in transacties:
    rij = tk.Frame(lijst_frame, bg="white")
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

# app starten
window.mainloop()