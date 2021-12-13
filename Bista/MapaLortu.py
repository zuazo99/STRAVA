import tkinter as tk
import urllib.parse
import urllib3
from PIL import Image, ImageTk
import io
import matplotlib.pyplot as plt


class Leioa():
    def __init__(self,poly):
        self.window = tk.Tk()
        self.window.title("Argazia")
        lbl=tk.Label(self.window, text="Argazkia")
        lbl.pack(side=tk.TOP)
        self.argazkiaTxertatu(poly)
        self.window.mainloop()
    def argazkiaTxertatu(self,poly):
        mapa_polyline =poly
        token = "pk.eyJ1IjoiZ29ya2FkcmEiLCJhIjoiY2t4NDU1ZXFiMTJnMTMwdXF4OGc2bXQzNyJ9.CdSMqExqBsfssVb2CtXBiA"
        strokeWidth = 1
        strokeColor = "f44"
        http = urllib3.PoolManager()
        polyline_ = urllib.parse.quote_plus(mapa_polyline)
        path = f"path-{strokeWidth}+{strokeColor}({polyline_})"
        host = "https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/"
        tamaina = "/auto/500x300"
        url = f"{host}{path}{tamaina}?access_token={token}"
        em = http.request('GET', url)
        # Irudiaren data irakurri eta argazkia sortu
        img = Image.open(io.BytesIO(em.data))
        # Tkinter en argazkia sortu
        # oso importantea self ekin gordetzea, bestela argazkia ezabatu egingo␣
        self.img2 = ImageTk.PhotoImage(img)
        # Label batean sartu
        panel = tk.Label(self.window, image=self.img2)
        # bistaratu
        panel.pack(side=tk.TOP)