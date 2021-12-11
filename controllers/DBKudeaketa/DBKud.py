import sqlite3
import datetime

#https://www.sqlitetutorial.net/sqlite-date/

class DBKudeaketa:

    def datuBaseKonexioa(self):
        try:
            sqliteConnection = sqlite3.connect('AktibitateaInfo.db')
            #cursor = sqliteConnection.cursor()
            print("Konexioa ondo")
            #hemen sql kontsultak exekutatuko dira

            #Datuak kontsultatu
            #query = "SELECT ekipamenduMat FROM Erabiltzailea WHERE erabID = "AQUI METEMOS EL ERABILTZAILE @";";



            #El primer imput de data es data1 y el segundo data2
            #query = "SELECT * FROM Informazioa fecha BETWEEN 'data1' AND 'data2'";
            #sqlite_select_kontsulta ="select sqlite_version();"
            #cursor.execute(sqlite_select_kontsulta)
            #erantzuna = cursor.fetchall()
            #print(erantzuna)
            return sqliteConnection


        except sqlite3.Error as error:

            print("Errorea konekzioa egiten sqlite")

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
        MATERIALA KUDEATU
    '''

    def materialaDagoenKonprobatu(self, datua):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT materiala FROM Ekipamendua WHERE materiala = ? ;"
        cursor.execute(query, [datua])
        erantzuna = cursor.fetchall()
        return len(erantzuna)

    def materialaSartu(self, datua):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Ekipamendua(materiala) VALUES(?)"
        cursor.execute(query, [datua])
        konexioa.commit()
        print("Materiala ondo gordeta")

    def materialaEzabatu(self):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "DELETE FROM Ekipamendua WHERE materiala = 'Nike Air Zoom Pegasus 37';"
        cursor.execute(query)
        konexioa.commit()
        print("Ondo ezabatu da")

    def materialaKontsultatu(self):
        konexioa = self.datuBaseKonexioa()
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


    '''
        ATLETA KUDEATU
    '''

    def atletaDagoenKonprobatu(self, id):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "SELECT erabID FROM Erabiltzailea WHERE erabID = ? ;"
        cursor.execute(query, [id])
        erantzuna = cursor.fetchall()
        return len(erantzuna)

    def atletaSartu(self, datuak):
        konexioa=self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Erabiltzailea(erabID, izena, abizena, ekipamenduMat) VALUES(?,?,?,?)"
        cursor.execute(query, datuak)
        #cursor.execute(query, [id, izena, abizena])
        konexioa.commit()
        cursor.close()
        print("Ondo gordeta")

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

    '''
            ENTRENAMENDUA KUDEATU
    '''

    def EntrenamenduaSartu(self, datuak):
        konexioa=self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Entrenamendua(ID, mota, data, km, denbora, ordua, entrErabId) " \
                "VALUES(?,?,?,?,?,?,?)"
        cursor.execute(query, datuak)
        #cursor.execute(query, [id, izena, abizena])
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

    '''
                MEDIZIOAK KUDEATU
        '''

    def medizioakSartu(self, datuak):
        konexioa=self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Medizioak(posizioa, abiadura, pultsazioak, entreData, entreOrdua, idEntrenamendua) " \
                "VALUES(?,?,?,?,?,?)"
        cursor.execute(query, datuak)
        #cursor.execute(query, [id, izena, abizena])
        konexioa.commit()
        cursor.close()
        print("Ondo gordeta")