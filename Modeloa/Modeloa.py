from Kontroladorea.StravaAPI import StravaAPIKud
from Kontroladorea.DBKudeaketa import DBKud
import datetime
#Para seguir el patron MVC:
#https://www.giacomodebidda.com/posts/mvc-pattern-in-python-sqlite/

class Modeloa:
    def main(self):

        DatuBasea = DBKud.DBKudeaketa()
        stravaApiKud = StravaAPIKud.StravaAPIKud()
        DatuBasea.datuBaseKonexioa()

        #API-ra konektatzeko.
        stravaApiKud.getAccessToTheAPI()
        print(" ")
        print("1. Get Athlete: ")
        print(" ")
        atletaInfo = stravaApiKud.getAthlete()
        print(stravaApiKud.getAthlete()) #Atletaren informazioa lortu. {'id': 61350307, 'firstname' : 'Mikel'....}
        print("ID_Atleta: ", atletaInfo['id'])
        print("Atleta ID_Materiala:", atletaInfo['shoes'][0]['id'])
        print("Materiala izena:", atletaInfo['shoes'][0]['name'])
        print("Bizikleta datuak", atletaInfo['bikes'])

        DatuBasea.materialaUpdate(atletaInfo['shoes'][0]['name'])

        '''
        if DatuBasea.materialaDagoenKonprobatu(atletaInfo['shoes'][0]['name']) == 0:
            DatuBasea.materialaSartu(atletaInfo['shoes'][0]['name'])
        '''

        #datuakAtleta = (atletaInfo['id'], atletaInfo['firstname'], atletaInfo['lastname'], atletaInfo['shoes'][0]['name'])

        datuakAtletaUpdate = (atletaInfo['id'], atletaInfo['firstname'], atletaInfo['lastname'], atletaInfo['shoes'][0]['name'], atletaInfo['id'])
        DatuBasea.atletaUpdate(datuakAtletaUpdate)

        '''
        if DatuBasea.atletaDagoenKonprobatu(atletaInfo['id']) == 0:
            DatuBasea.atletaSartu(datuakAtleta)
        DatuBasea.atletaKontsultatu()
        '''

        print(" ")
        print("2. Get AthleteActivities: ")
        print(" ")
        em = stravaApiKud.getAthleteActivities() #Returns the activities of an athlete. [{"resource_state : 2, "athlete : {"id" : 1234}, "id" : 123456}]
        print(em)

        print(" ")
        print("3. Get ActivityById: ")
        print(" ")
        print("4. Get ActivityStreams: ")
        print(" ")
        indizea = 1
        for aktibitatea in em:
            print(str(indizea) + ". Aktibitatea")
            print("IDa: " + str(aktibitatea["id"]))
            print("Mota", aktibitatea['type'])
            dataOrdua = str(aktibitatea['start_date']).split('T')
            data = dataOrdua[0]
            ordua = dataOrdua[1].replace('Z', '')
            print("Data", data)
            print("Ordua", ordua)
            kilometroak = int(aktibitatea['distance']) / 1000
            print("Kilometroak", kilometroak)
            denbora = str(datetime.timedelta(seconds=aktibitatea['elapsed_time']))
            print("denbora", denbora)
            print("erabID", atletaInfo['id'])

            aktibitateaID = stravaApiKud.getActivietesById(aktibitatea["id"])
            print("Ekipamendua ID:", aktibitateaID['gear_id'])
            ekipamenduaID = aktibitateaID['gear_id']
            ekipamenduTot = "A"
            if ekipamenduaID is None:
                ekipamenduTot = "X"

            else:
                ekipamendua = stravaApiKud.getGearsById(ekipamenduaID)
                ekipamenduMarca = ekipamendua['brand_name']
                ekipamenduModelo = ekipamendua['model_name']
                ekipamenduTot = ekipamenduMarca+" "+ekipamenduModelo
            print(ekipamenduTot)
            #datos = (aktibitatea["id"], aktibitatea['type'], data, kilometroak, denbora, ordua, atletaInfo['id'], ekipamenduTot)
            datosUpdate = (aktibitatea["id"], aktibitatea['type'], data, kilometroak, denbora, ordua, atletaInfo['id'], ekipamenduTot, aktibitatea["id"])
            DatuBasea.entrenamenduaUpdate(datosUpdate)
            '''
                if DatuBasea.entrenamenduaDagoenKonprobatu(aktibitatea["id"]) == 0:
                    DatuBasea.EntrenamenduaSartu(datos)
                    
            '''


            if aktibitatea['has_heartrate'] is False:
                aktibitatea['average_heartrate'] = 0.0

            print("Posizioa", aktibitatea['start_latlng'])
            print("Abiadura", aktibitatea['average_speed'])
            print("pultsazioak", aktibitatea['average_heartrate'])
            print("entreData", data)
            print("entreOrdua", ordua)
            print("idEntrenamendua", aktibitatea["id"])
            latilng=' '.join(str(e) for e in aktibitatea['start_latlng'])


            #medizioak = (latilng, aktibitatea['average_speed'], aktibitatea['average_heartrate'], data, ordua, aktibitatea["id"])
            medizioakUpdate = (latilng, aktibitatea['average_speed'], aktibitatea['average_heartrate'], data, ordua, aktibitatea["id"], aktibitatea["id"])
            DatuBasea.medizioakUpdate(medizioakUpdate)

            '''
            if DatuBasea.medizioakDagoenKonprobatu(aktibitatea["id"]):
                DatuBasea.medizioakSartu(medizioak)
            '''
           # aktibitateaID = stravaApiKud.getActivietesById(aktibitatea["id"])
            '''
            SEGMENTUAK LORTU
            '''
            print("ID segmentua:", aktibitateaID['id'])
            print("Kudos:", aktibitateaID['kudos_count'])
            if not aktibitateaID['segment_efforts']:
                print("Segmentua hutsik dago")
            else:
                print("Segmentua ID:", aktibitateaID['segment_efforts'])
                print("Segmentua izena:", aktibitateaID['segment_efforts'][0]['name'])
                denboraSegmentua = str(datetime.timedelta(seconds=aktibitateaID['segment_efforts'][0]['elapsed_time']))
                print("Segmentua denbora:", denboraSegmentua)
                distantziaSegmentua = aktibitateaID['segment_efforts'][0]['distance']/1000
                print("Segmentua distantzia:", distantziaSegmentua)
                print("ID aktibitatea")

                datosSegmentua = (aktibitateaID['segment_efforts'][0]['name'], denboraSegmentua, aktibitatea["id"], distantziaSegmentua)
                datosSegmentoKomprobatu = (aktibitateaID['segment_efforts'][0]['name'], denboraSegmentua)
                if DatuBasea.SegmentuakDagoenKonprobatu(datosSegmentoKomprobatu) == 0:
                    DatuBasea.SegmentuakSartu(datosSegmentua)


            '''
                BUELTAK LORTU
            '''

            if not aktibitateaID['laps']:
                print("Aktibitatea ez ditu bueltarik")
            else:
                bueltak = stravaApiKud.getLapsById(aktibitatea["id"])
                print("Bueltak:", bueltak)
                for buelta in bueltak:
                    print("Buelta index", buelta['lap_index'])
                    print("Buelta izena", buelta['name'])
                    denboraBuelta = str(datetime.timedelta(seconds=buelta['elapsed_time']))
                    print("Denbora", buelta['elapsed_time'])
                    print("km", buelta['distance'])
                    kilometroak = buelta['distance']/1000
                    print("abiaduraMax", buelta['max_speed'])
                    print("erritmoa", buelta['average_speed'])
                    print("entrenaID", buelta['activity']['id'])

                    bueltaDatuak = (buelta['lap_index'], buelta['name'], denboraBuelta, kilometroak, buelta['max_speed'], buelta['average_speed'], buelta['activity']['id'])
                    #if DatuBasea.BueltaDagoenKonprobatu(buelta['lap_index']) == 0:
                    DatuBasea.BueltaSartu(bueltaDatuak)


            indizea = indizea + 1
            print(" ")
            '''
            print("Informazioa->")
            print(" --- ")
            aktibitateInfo = stravaApiKud.getActivityStreams(em[indizea-1]["id"], ["time", "distance", "latlng", "altitude",
                                                                                   "velocity_smooth", "heartrate", "cadence", "watts", "temp", "moving", "grade_smooth"])
    
            print("AKTIbitate_INfo")
            print(aktibitateInfo)
    
        
            for e in aktibitateInfo:
                d = aktibitateInfo[e]["data"]
                print("D aldagaia")
                print(d)
                luzera = len(d)
                for segundua in range(luzera-1):
                    print(e, d[segundua])
    
                    # Hemen joango zen SQL Insert-a
            print(" --- ")
            print(" ")
        '''
