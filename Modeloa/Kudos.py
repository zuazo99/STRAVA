from Kontroladorea.DBKudeaketa.DBKud import dbKudeaketa


class Kudos:
    def __init__(self):
        print()
        self.dbKudeaketa = dbKudeaketa

    def KudosSartu(self, datuak):
        konexioa = self.dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Kudos(ErabID, EntrenaID) VALUES(?, ?);";
        cursor.execute(query, datuak)
        #cursor.execute(query, [id, izena, abizena])
        konexioa.commit()
        cursor.close()
        print("Ondo gordeta")

    def KudosKonprobatu(self, datuak):
        konexioa = self.dbKudeaketa.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT * FROM Kudos;";
        cursor.execute(query, datuak)
        erantzuna = cursor.fetchall()
        return len(erantzuna)