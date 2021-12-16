from Kontroladorea.DBKudeaketa.DBKud import dbKudeaketa

class Entrenamendua:
    def __init__(self):
        print()
        self.dbKudeaketa = dbKudeaketa

    def EntrenamenduaSartu(self, datuak):
        konexioa=self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Entrenamendua(ID, mota, data, km, denbora, ordua, entrErabId, erabilitakoMateriala) " \
                "VALUES(?,?,?,?,?,?,?,?)"
        cursor.execute(query, datuak)
        konexioa.commit()
        cursor.close()
        print("Ondo gordeta")

    def entrenamenduaDagoenKonprobatu(self, id):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT ID FROM Entrenamendua WHERE ID = ? ;"
        cursor.execute(query, [id])
        erantzuna = cursor.fetchall()
        return len(erantzuna)

    def entrenamenduaDatenArteanLortu(self, datak):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT * FROM Entrenamendua WHERE data BETWEEN ? AND ? ;"
        cursor.execute(query, datak)
        erantzuna = cursor.fetchall()
        return erantzuna

    '''
    def entrenamenduaIDLortu(self, id):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        self.erantzuna = []
        query = "SELECT e.* FROM Entrenamendua AS e WHERE e.ID = ? ;"
        cursor.execute(query, id)
        self.erantzuna.append(cursor.fetchall())
        query = "SELECT b.* FROM Entrenamendua AS e, Buelta AS b WHERE b.entreData = e.data, m.entreOrdua = e.ordua AND e.ID = ?;"
        cursor.execute(query, id)
        self.erantzuna.append(cursor.fetchall())
        query = "SELECT m.posizioa, m.AVG(abiadura), m.AV(pultsazioak), m.entreOrdua, m.entreData , idEntrenamendua FROM Medizioak AS m WHERE m.idEntrenamendua = ? ;"
        cursor.execute(query, id)
        self.erantzuna.append(cursor.fetchall())
        query = "SELECT s.* FROM Segmentua AS s WHERE s.idEntrenamendua= ? ;"
        cursor.execute(query, id)
        self.erantzuna.append(cursor.fetchall())
        return erantzuna
    '''
    def entrenamenduaUpdate(self, datuak):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "UPDATE Entrenamendua SET ID = ?, mota = ?, data = ?, km = ?, denbora = ?, ordua = ?, entrErabId = ?, erabilitakoMateriala = ? WHERE id = ?;"
        cursor.execute(query, datuak)
        konexioa.commit()
        cursor.close()
        print("Ondo aldatuta")