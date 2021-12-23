
from Kontroladorea.DBKudeaketa import dbKudeaketa

class Buelta:
    def __init__(self):
        print()
        self.dbKudeaketa = dbKudeaketa

    def BueltaSartu(self, datuak):
        konexioa=self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Buelta(izena, denbora, km, abiaduraMax, erritmoa, entrenaID) VALUES(?,?,?,?,?,?) ;"

        cursor.execute(query, datuak)
        konexioa.commit()
        cursor.close()
        print("Ondo gordeta")

    def BueltaDagoenKonprobatu(self, datuak):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT izena FROM Buelta WHERE izena = ? AND entrenaID = ? ;"
        cursor.execute(query, datuak)
        erantzuna = cursor.fetchall()
        return len(erantzuna)