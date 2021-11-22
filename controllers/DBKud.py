import sqlite3




def datuBaseKud():
    try:
        sqliteConnection = sqlite3.connect('AktibitateInfo.db')
        cursor = sqliteConnection.cursor()
        print("Konexioa ondo")
        #hemen sql kontsultak exekutatuko dira

        sqlite_select_kontsulta =" select sqlite_version();"
        cursor.execute(sqlite_select_kontsulta)
        erantzuna = cursor.fetchall()
        print("SQLite bersioa:", erantzuna)

        cursor.close()


    except sqlite3.Error as error:

        print("Errorea konekzioa egiten sqlite")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("SQLite konexioa itzi egin da")

