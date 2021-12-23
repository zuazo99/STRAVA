
from Kontroladorea.DBKudeaketa import dbKudeaketa


class Iruzkina:
    def __init__(self):
        print()
        self.dbKudeaketa = dbKudeaketa


    def IruzkinaKudeatu(self, datuak):
        konexioa = self.dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Iruzkina(id, testua) VALUES (?,?)";
        cursor.execute(query, datuak)
        #cursor.execute(query, [id, izena, abizena])
        konexioa.commit()
        cursor.close()
        print("Ondo gordeta")

    def IruzkinaKonprobatu(self, datuak):
        konexioa = self.dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT * FROM Iruzkina WHERE id = ? AND testua = ?;";
        cursor.execute(query, datuak)
        erantzuna = cursor.fetchall()
        return len(erantzuna)