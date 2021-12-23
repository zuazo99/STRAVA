
from Kontroladorea.DBKudeaketa import dbKudeaketa

class Materiala:


    def materialaEzabatu(self):
        konexioa = dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "DELETE FROM Ekipamendua WHERE materiala = 'Nike Air Zoom Pegasus 37';"
        cursor.execute(query)
        konexioa.commit()
        print("Ondo ezabatu da")

    def materialaDagoenKonprobatu(self, datua):
        konexioa = dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT materiala FROM Ekipamendua WHERE materiala = ? ;"
        cursor.execute(query, [datua])
        erantzuna = cursor.fetchall()
        return len(erantzuna)

    def materialaSartu(self, datua):
        konexioa = dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Ekipamendua(materiala) VALUES(?)"
        cursor.execute(query, [datua])
        konexioa.commit()
        print("Materiala ondo gordeta")

    def materialaUpdate(self, datua):
        konexioa = dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "UPDATE Ekipamendua SET materiala = ?  ;"
        cursor.execute(query, [datua])
        konexioa.commit()
        cursor.close()
        print("Ondo aldatuta")
    def materialaKontsultatu(self):
        konexioa = dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT * FROM Ekipamendua;"
        cursor.execute(query)
        ekipamenduIzena = cursor.fetchall()
        print(ekipamenduIzena)
        print("+{:-<50}+".format(""))
        print("|{:^50}|".format("materiala"))
        print("+{:-<50}+".format(""))

        for materiala, in ekipamenduIzena:
            print("|{:^50}|".format(materiala))

        print("+{:-<50}+".format(""))

    def materialKmLortu(self):

        konexioa = dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT SUM(KM),erabilitakoMateriala FROM Entrenamendua GROUP BY erabilitakoMateriala ;"
        cursor.execute(query)
        erantzuna = cursor.fetchall()
        return erantzuna
