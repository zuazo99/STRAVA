from Kontroladorea.DBKudeaketa import dbKudeaketa

class Segmentuak:
    def __init__(self):
        print()
        self.dbKudeaketa = dbKudeaketa

    def SegmentuakSartu(self, datuak):
        konexioa=self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Segmentua(izena, denbora, idEntrenamendua, distantzia) " \
                "VALUES(?,?,?,?)"
        cursor.execute(query, datuak)
        #cursor.execute(query, [id, izena, abizena])
        konexioa.commit()
        cursor.close()
        print("Ondo gordeta")

    def SegmentuakDagoenKonprobatu(self, datuak):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT izena,denbora FROM Segmentua WHERE izena = ? AND denbora = ? ;"
        cursor.execute(query, datuak)
        erantzuna = cursor.fetchall()
        return len(erantzuna)

    def SegmentuakUpdate(self, datuak):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "UPDATE Segmentua SET izena = ?, denbora = ?, idEntrenamendua = ?, distantzia = ? WHERE idEntrenamendua = ?,  ;"
        cursor.execute(query, datuak)
        konexioa.commit()
        cursor.close()
        print("Ondo aldatuta")
