import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import controllers.DBKud as db

#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?codigo=82
#https://www.programadornovato.com/colocar-datos-de-nuestra-base-de-datos-en-nuestra-tabla-treeview-con-python-y-tkinter-06/

class pantallitas:
    def __init__(self):
        self.datuak=db.DBKudeaketa()
        print("pasa de datuak")
        self.window=tk.Tk()
        self.window.title("STRAVass")
        self.cuaderno=ttk.Notebook(self.window)
        print("entra login")
        self.login()
        print("sale de login")
        self.cuaderno.grid(column=0, row=0, padx=10, pady=10)
        self.window.mainloop()
        print("aaaaah")
    def login(self):
        print("aaaaah")
        self.pagina1 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina1, text="Carga de artículos")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Artículo")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1 = ttk.Label(self.labelframe1, text="Descripción:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga = tk.StringVar()
        self.entrydescripcion = ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        self.label2 = ttk.Label(self.labelframe1, text="Precio:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.preciocarga = tk.StringVar()
        self.entryprecio = ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)
        self.boton1 = ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        print("aaaaah")

pantallitas()