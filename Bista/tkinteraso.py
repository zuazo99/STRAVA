import tkinter as tk
from tkinter import ttk
from Kontroladorea import DBKudeaketa as db
from . import Leioa

#Habria que sacar el modelo de esta clase nenes


#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?codigo=82
#https://www.programadornovato.com/colocar-datos-de-nuestra-base-de-datos-en-nuestra-tabla-treeview-con-python-y-tkinter-06/

class pantallitas:

    def __init__(self):
        self.datuak=db.DBKudeaketa()
        print("pasa de datuak")
        self.window=tk.Tk()
        self.window.title("STRAVA Interfazea")
        self.cuaderno=ttk.Notebook(self.window)
        print("entra login")
        self.datuak_freskatu()
        self.materiala_kontsultatu()
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


    def materiala_kontsultatu(self):
        print("aaaaah")
        self.pagina2 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina2, text="Materiala kontsultatu")
        self.boton2 = ttk.Button(self.pagina2, text="Kontsultatu", command=self.material)
        self.boton2.grid(column=1, row=2, padx=4, pady=4)

    def material(self):
        print("Imprimimos debajo del botón el material que tenemos y cuantos km hemos hecho con ellos")
        self.material = self.datuak.materialKmLortu()
        self.goiburuak = ["Ekipamendua", "KM-ak"]
        self.datuak = []
        for self.mat in self.material:
            self.datuak.append([self.mat[1], self.mat[0]])
        print(self.datuak)
        Leioa.Leioa(self.goiburuak, self.datuak)



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
        self.boton1 = ttk.Button(self.labelframe3, text="Balioztatu", command=self.konts_data)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def konts_data(self):
        print("imprimimos las actividades hechas entre las fechas seleccionadas")
        #SELECT * FROM entrenamientos WHERE data BETWEEN %noiztik AND %nora
        print(self.noiztik.get())
        print(self.nora.get())
        self.datak = []
        self.datak.append(self.noiztik.get())
        self.datak.append(self.nora.get())
        print(self.datak)
        self.entr = self.datuak.entrenamenduaDatenArteanLortu(datak)
        self.goiburuak = ["ID", "mota", "data", "km", "denbora", "ordua", "Erabiltzailearen Id-a", "Erabilitako materiala"]
        self.datuak = []
        for self.mat in self.entr:
            self.datuak.append([self.mat[0], self.mat[1], self.mat[2],self.mat[3], self.mat[4], self.mat[5], self.mat[6], self.mat[7]])
        Leioa.Leioa(self.goiburuak, self.datuak)

#pantallitas()