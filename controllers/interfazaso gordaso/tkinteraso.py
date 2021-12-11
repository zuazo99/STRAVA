import tkinter as tk
from tkinter import ttk
import controllers.DBKudeaketa.DBKud as db

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
        self.datuak_freskatu()
        self.materiala_kontzultatu()
        self.data_bidez_kontsulta()
        print("sale de login")
        self.cuaderno.grid(column=0, row=0, padx=10, pady=10)
        self.window.mainloop()
        print("aaaaah")
    def datuak_freskatu(self):
        print("aaaaah")
        self.pagina1 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina1, text="Datuak freskatu")
        self.boton1 = ttk.Button(self.pagina1, text="Freskatu", command=self.freskatu)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def freskatu(self):
        print("Aqui cogemos los 30 ultimos eventos de la api de strava y si no están ya metidos en la db los añadimos, si están pasamos")


    def materiala_kontzultatu(self):
        print("aaaaah")
        self.pagina2 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina2, text="Materiala kontsultatu")
        self.boton2 = ttk.Button(self.pagina2, text="Kontsultatu", command=self.material)
        self.boton2.grid(column=1, row=2, padx=4, pady=4)

    def material(self):
        print("Imprimimos debajo del botón el material que tenemos y cuantos km hemos hecho con ellos")

    def data_bidez_kontsulta(self):
        print("aaaaah")
        self.pagina3 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina3, text="Data bidez kontsultatu")
        self.labelframe3 = ttk.LabelFrame(self.pagina3, text="Tartea")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.label1 = ttk.Label(self.labelframe3, text="Noiztik:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.noiztik = tk.StringVar()
        self.entryNoiztik = ttk.Entry(self.labelframe3, textvariable=self.noiztik)
        self.entryNoiztik.grid(column=1, row=0, padx=4, pady=4)
        self.label2 = ttk.Label(self.labelframe3, text="Nora:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nora = tk.StringVar()
        self.entryNora = ttk.Entry(self.labelframe3, textvariable=self.nora)
        self.entryNora.grid(column=1, row=1, padx=4, pady=4)
        self.boton1 = ttk.Button(self.labelframe3, text="Balioztatu", command=self.kontz_data)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def kontz_data(self):
        print("imprimimos las actividades hechas entre las fechas seleccionadas")
        #SELECT * FROM entrenamientos WHERE data BETWEEN %noiztik AND %nora
        print(self.noiztik.get())
        print(self.nora.get())

pantallitas()