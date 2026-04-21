import tkinter as tk
from tkinter import messagebox

# ---- "DATABASE" ----
gebruiker_naam = "Alex"
saldo = 1250.00

# ---- VENSTER ----
window = tk.Tk()
window.title("Bankapp Dashboard")
window.geometry("500x400")
window.configure(bg="#333333")
window.minsize(500, 500)
window.maxsize(700, 600)

# ---- HELPERS ----
def format_euro(bedrag):
    return f"€ {bedrag:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

saldo_var = tk.StringVar(value=format_euro(saldo))

def transactie(modus):
    global saldo
    invoer = bedrag_invoer.get().strip().replace(",", ".")
    try:
        bedrag = float(invoer)
        if bedrag <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Fout", "Voer een geldig bedrag in.")
        return

    if modus == "opname" and bedrag > saldo:
        messagebox.showerror("Fout", "Onvoldoende saldo.")
        return

    saldo += bedrag if modus == "storting" else -bedrag
    saldo_var.set(format_euro(saldo))
    bedrag_invoer.delete(0, tk.END)
    messagebox.showinfo("Geslaagd", f"{'Gestort' if modus == 'storting' else 'Opgenomen'}: {format_euro(bedrag)}")

# ---- UI ----
tk.Label(window, text="Home / Dashboard", font=("Arial", 18, "bold"), bg="#333333", fg="white").pack(pady=10)
tk.Label(window, text=f"Goedemiddag, {gebruiker_naam}", font=("Arial", 14), bg="white", width=30, height=2, relief="solid").pack(pady=5)
tk.Label(window, textvariable=saldo_var, font=("Arial", 24, "bold"), bg="white", width=15, height=2, relief="solid").pack(pady=10)

# Bedrag invoer
bedrag_invoer = tk.Entry(window, font=("Arial", 14), justify="center", width=15)
bedrag_invoer.pack(pady=5)

# Knoppen
knoppen_frame = tk.Frame(window, bg="#333333")
knoppen_frame.pack(pady=10)

tk.Button(knoppen_frame, text="Storten",  width=15, height=2, bg="#0000FF", fg="white", activebackground="#0000CC", command=lambda: transactie("storting")).grid(row=0, column=0, padx=5)
tk.Button(knoppen_frame, text="Opnemen", width=15, height=2, bg="#0000FF", fg="white", activebackground="#0000CC", command=lambda: transactie("opname")).grid(row=0, column=1, padx=5)

window.mainloop()