import sqlite3
import datetime
from Modeloa import *
#https://www.sqlitetutorial.net/sqlite-date/
import Modeloa


class DBKudeaketa:

    def datuBaseKonexioa(self):
        try:
            sqliteConnection = sqlite3.connect('AktibitateaInfo.db')
            print("Konexioa ondo")
            return sqliteConnection

        except sqlite3.Error as error:
            print("Errorea konexioa egiten sqlite-rekin")
        #finally:
           #if sqliteConnection:
            #  sqliteConnection.close()
             #  print("SQLite konexioa itzi egin da")

    def datuBaseaKonexioaItxi(self):
        sqliteConnection = self.datuBaseKonexioa()
        if sqliteConnection:
            sqliteConnection.close()
            print("SQLite konexioa itzi egin da")




    '''
        ------------------------------- MATERIALA KUDEATU -------------------------------
    '''
    materiala = Modeloa.Materiala()
    materiala.materialaDagoenKonprobatu()
    materiala.materialaSartu()
    materiala.materialaUpdate()
    materiala.materialaEzabatu()
    materiala.materialaKontsultatu()
    materiala.materialKmLortu()




    '''
        ------------------------------- ATLETA KUDEATU -------------------------------
    '''

    atleta = Modeloa.Atleta()
    atleta.atletaSartu()
    atleta.atletaEzabatu()
    atleta.atletaUpdate()
    atleta.atletaDagoenKonprobatu()
    atleta.atletaKontsultatu()

    '''
        ------------------------------- ENTRENAMENDUA KUDEATU -------------------------------
    '''

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

    def entrenamenduaUpdate(self, datuak):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "UPDATE Entrenamendua SET ID = ?, mota = ?, data = ?, km = ?, denbora = ?, ordua = ?, entrErabId = ?, erabilitakoMateriala = ? WHERE id = ?;"
        cursor.execute(query, datuak)
        konexioa.commit()
        cursor.close()
        print("Ondo aldatuta")

    '''
        ------------------------------- MEDIZIOAK KUDEATU -------------------------------
    '''

    def medizioakSartu(self, datuak):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Medizioak(posizioa, abiadura, pultsazioak, entreData, entreOrdua, idEntrenamendua) " \
                "VALUES(?,?,?,?,?,?)"
        cursor.execute(query, datuak)
        #cursor.execute(query, [id, izena, abizena])
        konexioa.commit()
        cursor.close()
        print("Ondo gordeta")

    def medizioakDagoenKonprobatu(self, id):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT idEntrenamendua FROM Medizioak WHERE idEntrenamendua = ? ;"
        cursor.execute(query, [id])
        erantzuna = cursor.fetchall()
        return len(erantzuna)

    def medizioakUpdate(self, datuak):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "UPDATE Medizioak SET posizioa = ?, abiadura = ?, pultsazioak = ?, entreData = ?, entreOrdua = ?, idEntrenamendua = ? WHERE idEntrenamendua = ? ;"
        cursor.execute(query, datuak)
        konexioa.commit()
        cursor.close()
        print("Ondo aldatuta")

    '''
        ------------------------------- SEGMENTUAK KUDEATU -------------------------------
    '''
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


    '''
        ------------------------------- KUDOS KUDEATU -------------------------------
    '''
    def KudosSartu(self, datuak):
        konexioa=self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Kudos(ErabID, EntrenaID) VALUES(?, ?);";
        cursor.execute(query, datuak)
        #cursor.execute(query, [id, izena, abizena])
        konexioa.commit()
        cursor.close()
        print("Ondo gordeta")

    def KudosKonprobatu(self, datuak):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT * FROM Kudos;";
        cursor.execute(query, datuak)
        erantzuna = cursor.fetchall()
        return len(erantzuna)
    '''
        ------------------------------- IRUZKINA KUDEATU -------------------------------
    '''
    def IruzkinaKudeatu(self, datuak):
        konexioa=self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Iruzkina(id, testua) VALUES (?,?)";
        cursor.execute(query, datuak)
        #cursor.execute(query, [id, izena, abizena])
        konexioa.commit()
        cursor.close()
        print("Ondo gordeta")

    def IruzkinaKonprobatu(self, datuak):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT * FROM Iruzkina WHERE id = ? AND testua = ?;";
        cursor.execute(query, datuak)
        erantzuna = cursor.fetchall()
        return len(erantzuna)

    '''
        BUELTAK KUDEATU
    '''
    buelta = Modeloa.Buelta()
    buelta.BueltaSartu()
    buelta.BueltaDagoenKonprobatu()


#SINGLETON PATRROIA
dbKudeaketa = DBKudeaketa()