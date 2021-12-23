import sqlite3

# https://www.sqlitetutorial.net/sqlite-date/
import Modeloa.Materiala


class DBKud:
    def __init__(self):
        self.materiala = Modeloa.Materiala

    def datuBaseKonexioa(self):
        try:
            sqliteConnection = sqlite3.connect('AktibitateaInfo.db')
            print("Konexioa ondo")
            return sqliteConnection

        except sqlite3.Error as error:
            print("Errorea konexioa egiten sqlite-rekin")
        # finally:
        # if sqliteConnection:
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

    #materiala = Modeloa.Materiala()

    def materialaDagoenKonprobatu(self, datua):
        self.materiala.materialaDagoenKonprobatu(datua)

    def materialaSartu(self, datua):
        self.materiala.materialaSartu(datua)

    def materialaUpdate(self, datua):
        self.materiala.materialaUpdate(datua)

    def materialaEzabatu(self):
        self.materiala.materialaEzabatu()

    def materialaKontsultatu(self):
        self.materiala.materialaKontsultatu()

    def materialaKmLortu(self):
        self.materiala.materialKmLortu()

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
    entrenamendua = Modeloa.Entrenamendua()
    entrenamendua.EntrenamenduaSartu()
    entrenamendua.entrenamenduaDagoenKonprobatu()
    entrenamendua.entrenamenduaUpdate()
    entrenamendua.entrenamenduaDatenArteanLortu()

    '''
        ------------------------------- MEDIZIOAK KUDEATU -------------------------------
    '''
    medizioak = Modeloa.Medizioak()
    medizioak.medizioakSartu()
    medizioak.medizioakUpdate()
    medizioak.medizioakDagoenKonprobatu()

    '''
        ------------------------------- SEGMENTUAK KUDEATU -------------------------------
    '''
    segmentuak = Modeloa.Segmentuak()
    segmentuak.SegmentuakSartu()
    segmentuak.SegmentuakUpdate()
    segmentuak.SegmentuakDagoenKonprobatu()

    '''
        ------------------------------- KUDOS KUDEATU -------------------------------
    '''
    kudos = Modeloa.Kudos()
    kudos.KudosSartu()
    kudos.KudosKonprobatu()
    '''
        ------------------------------- IRUZKINA KUDEATU -------------------------------
    '''
    iruzkina = Modeloa.Iruzkina()
    iruzkina.IruzkinaKudeatu()
    iruzkina.IruzkinaKonprobatu()

    '''
        BUELTAK KUDEATU
    '''
    buelta = Modeloa.Buelta()
    buelta.BueltaSartu()
    buelta.BueltaDagoenKonprobatu()


# SINGLETON PATRROIA
dbKudeaketa = DBKud()
