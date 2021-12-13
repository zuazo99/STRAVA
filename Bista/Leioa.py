import tkinter as tk
from tkinter import ttk


class Leioa():
    def __init__(self, goiburuak, datuak):
        self.window = tk.Tk()
        self.window.title("Erabilitako materiala")
        scroll = ScrollContainer(self.window)
        self.main_frame = scroll.second_frame

        if len(goiburuak)==2:
            self.taula = ttk.Treeview(self.main_frame, columns=(0, 1), show='headings')
        elif len(goiburuak)==8:
            self.taula = ttk.Treeview(self.main_frame, columns=(0, 1, 2, 3, 4, 5, 6, 7, 8), show='headings')
        else:
            self.taula = ttk.Treeview(self.main_frame, columns=(0, 1, 2), show='headings')
        self.taula.bind("<Double-1>", lambda ev: print(self.taula.selection()))
        ## Goiburu izenak sartu egiten dira.
        for i, g in enumerate(goiburuak):
            self.taula.column(f"#{i}", minwidth=0, width=200)
            self.taula.heading(i, text=g)
        ## Datuak taulan zartu
        for i, d in enumerate(datuak):
            self.taula.insert(parent='', index=i, iid=i, values=d)

        self.taula.pack()
        self.window.mainloop()
