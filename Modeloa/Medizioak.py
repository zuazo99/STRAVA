from Kontroladorea.DBKudeaketa.DBKud import dbKudeaketa

class Medizioak:
    def __init__(self):
        print()
        self.dbKudeaketa = dbKudeaketa

    def medizioakSartu(self, datuak):
        konexioa = self.dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Medizioak(posizioa, abiadura, pultsazioak, entreData, entreOrdua, idEntrenamendua) " \
                "VALUES(?,?,?,?,?,?)"
        cursor.execute(query, datuak)
        #cursor.execute(query, [id, izena, abizena])
        konexioa.commit()
        cursor.close()
        print("Ondo gordeta")

    def medizioakDagoenKonprobatu(self, id):
        konexioa = self.dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT idEntrenamendua FROM Medizioak WHERE idEntrenamendua = ? ;"
        cursor.execute(query, [id])
        erantzuna = cursor.fetchall()
        return len(erantzuna)

    def medizioakUpdate(self, datuak):
        konexioa = self.dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "UPDATE Medizioak SET posizioa = ?, abiadura = ?, pultsazioak = ?, entreData = ?, entreOrdua = ?, idEntrenamendua = ? WHERE idEntrenamendua = ? ;"
        cursor.execute(query, datuak)
        konexioa.commit()
        cursor.close()
        print("Ondo aldatuta")
