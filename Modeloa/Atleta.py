
from Kontroladorea.DBKudeaketa.DBKud import dbKudeaketa

class Atleta:
    def __init__(self):
        print()
        self.dbKudeaketa = dbKudeaketa


    def atletaDagoenKonprobatu(self, id):
        konexioa = self.dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT erabID FROM Erabiltzailea WHERE erabID = ? ;"
        cursor.execute(query, [id])
        erantzuna = cursor.fetchall()
        return len(erantzuna)

    def atletaSartu(self, datuak):
        konexioa = self.dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Erabiltzailea(erabID, izena, abizena, ekipamenduMat) VALUES(?,?,?,?)"
        cursor.execute(query, datuak)
        #cursor.execute(query, [id, izena, abizena])
        konexioa.commit()
        cursor.close()
        print("Ondo gordeta")

    def atletaUpdate(self, datuak):
        konexioa = self.dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "UPDATE Erabiltzailea SET erabID = ?, izena = ?, abizena = ?, ekipamenduMat = ? WHERE erabID = ? ;"
        cursor.execute(query, datuak)
        konexioa.commit()
        cursor.close()
        print("Ondo aldatuta")

    def atletaKontsultatu(self):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT * FROM Erabiltzailea;"
        cursor.execute(query)
        erabiltzailea = cursor.fetchall()
        # https://www.w3schools.com/python/ref_string_format.asp
        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "",""))
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("erabID", "izena", "abizena", "ekipamenduMat"))
        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", ""))

        for erabID, izena, abizena, ekipamenduMat in erabiltzailea:
            print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(erabID, izena, abizena, ekipamenduMat))

        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", ""))


    def atletaEzabatu(self):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = ""
        cursor.execute(query)
