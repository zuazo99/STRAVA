import sqlite3

#https://www.sqlitetutorial.net/sqlite-date/

class DBKudeaketa:

    def datuBaseKonexioa(self):
        try:
            sqliteConnection = sqlite3.connect('AktibitateaInfo.db')
            #cursor = sqliteConnection.cursor()
            print("Konexioa ondo")
            #hemen sql kontsultak exekutatuko dira

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

    def materialaSartu(self, datuak):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = "INSERT INTO Ekipamendua(materiala) VALUES(?)"
        cursor.execute(query, datuak)
        konexioa.commit()
        print("Materiala ondo gordeta")
    def atletaSartu(self, datuak):
        konexioa=self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query= "INSERT INTO Erabiltzailea(erabID, izena, abizena, ekipamenduMat) VALUES(?,?,?)"
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
        print("+{:-<20}+{:-<20}+{:-<20}+".format("", "", ""))
        print("|{:^20}|{:^20}|{:^20}|".format("erabID", "izena", "abizena"))
        print("+{:-<20}+{:-<20}+{:-<20}+".format("", "", ""))

        for erabID, izena, abizena in erabiltzailea:
            print("|{:^20}|{:^20}|{:^20}|".format(erabID, izena, abizena))

        print("+{:-<20}+{:-<20}+{:-<20}+".format("", "", ""))


    def tablakSortu(self):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()


    def atletaEzabatu(self):
        konexioa = self.datuBaseKonexioa()
        cursor = konexioa.cursor()
        query = ""
        cursor.execute(query)