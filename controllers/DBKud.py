import sqlite3


#class DBKudeaketa:

    def datuBaseKud():
        try:
            sqliteConnection = sqlite3.connect('AktibitateaInfo.db')
            cursor = sqliteConnection.cursor()
            print("Konexioa ondo")
            #hemen sql kontsultak exekutatuko dira

            sqlite_select_kontsulta ="select sqlite_version();"
            cursor.execute(sqlite_select_kontsulta)
            erantzuna = cursor.fetchall()

            #query= "INSERT INTO Erabiltzailea(erabID, izena, abizena) VALUES(?,?,?)"
            #cursor.execute(query, [id, izena, abizena])
            #sqliteConnection.commit()
            #print("Ondo gordeta")
            query2= "SELECT * FROM Erabiltzailea;"
            cursor.execute(query2)
            erabiltzailea = cursor.fetchall()
            #https://www.w3schools.com/python/ref_string_format.asp
            print("+{:-<20}+{:-<20}+{:-<20}+".format("", "", ""))
            print("|{:^20}|{:^20}|{:^20}|".format("erabID", "izena", "abizena"))
            print("+{:-<20}+{:-<20}+{:-<20}+".format("", "", ""))

            for erabID, izena, abizena in erabiltzailea:
                print("|{:^20}|{:^20}|{:^20}|".format(erabID, izena, abizena))

            print("+{:-<20}+{:-<20}+{:-<20}+".format("", "", ""))



            cursor.close()


        except sqlite3.Error as error:

            print("Errorea konekzioa egiten sqlite")
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("SQLite konexioa itzi egin da")


