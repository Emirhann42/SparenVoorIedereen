import tkinter as tk

from login import LoginScreen
from homescreen import HomeScreen
from instellingen import SettingsScreen
from rente_grafiek import RenteScreen
from transactie_geschiedenis import TransactiesScreen
from register import RegisterScreen


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("My App")
        self.geometry('360x450')

        self.frames = {}

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Add all screens
        for F in (LoginScreen, HomeScreen, SettingsScreen, RenteScreen, TransactiesScreen, RegisterScreen):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginScreen")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()