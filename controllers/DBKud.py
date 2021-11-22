import sqlite3

try:
    sqliteConnection = sqlite3.connect('Nombre_DB')
    cursor = sqliteConnection.cursor()
    #hemen sql kontsultak exekutatuko dira

except sqlite3.Error as error:

    print("Errorea konekzioa egiten sqlite")
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite konexioa itzi egin da")

