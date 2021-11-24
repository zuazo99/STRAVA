import sqlite3




def datuBaseKud(id,izena,abizena):
    try:
        sqliteConnection = sqlite3.connect('AktibitateaInfo.db')
        cursor = sqliteConnection.cursor()
        print("Konexioa ondo")
        #hemen sql kontsultak exekutatuko dira

        sqlite_select_kontsulta =" select sqlite_version();"
        cursor.execute(sqlite_select_kontsulta)
        erantzuna = cursor.fetchall()

        query= "INSERT INTO Erabiltzailea(erabID, izena, abizena) VALUES(?,?,?)"
        cursor.execute(query, [id, izena, abizena])
        sqliteConnection.commit()
        print("Ondo gordeta")
        query2= "SELECT * FROM Erabiltzailea;"
        cursor.execute(query2)
        erabiltzailea = cursor.fetchall()
        print("Kontsulta")
        print(erabiltzailea)



        cursor.close()


    except sqlite3.Error as error:

        print("Errorea konekzioa egiten sqlite")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("SQLite konexioa itzi egin da")

