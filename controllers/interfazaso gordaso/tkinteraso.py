import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import controllers.DBKud as db



class pantallitas:
    def __init__(self):
        self.datuak=db.DBKudeaketa()
        self.window=tk.Tk()
        self.window.geometry('500x400')
        self.window.title("STRAVass")
        self.testua = tk.Label(self.window, text="gaur txalupen etorri gea")
        self.testua.pack()
        self.window.mainloop()
    def login(self):
