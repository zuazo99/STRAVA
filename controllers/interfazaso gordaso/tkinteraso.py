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
        self.window=tk.Tk()
        self.window.geometry('500x400')
        self.window.title("STRAVass")
        self.testua = tk.Label(self.window, text="gaur txalupen etorri gea")
        self.testua.pack()
        self.window.mainloop()
    #def login(self):
