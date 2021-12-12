from controllers.StravaAPI import stravaApiKud
from controllers.DBKudeaketa import DBKud
import datetime
# kaixo



if __name__ == '__main__':

    print(" ")
    print("Konexioa egiten APIarekin: ")
    print(" ")
    DatuBasea = DBKud.DBKudeaketa()
    print("Datu Basearekin konexioa:")
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

    if DatuBasea.materialaDagoenKonprobatu(atletaInfo['shoes'][0]['name']) == 0:
        DatuBasea.materialaSartu(atletaInfo['shoes'][0]['name'])
    DatuBasea.materialaKontsultatu()

    datuak = (atletaInfo['id'], atletaInfo['firstname'], atletaInfo['lastname'], atletaInfo['shoes'][0]['name'])

    if DatuBasea.atletaDagoenKonprobatu(atletaInfo['id']) == 0:
        DatuBasea.atletaSartu(datuak)
    DatuBasea.atletaKontsultatu()

    print(" ")
    print("2. Get AthleteActivities: ")
    print(" ")
    em = stravaApiKud.getAthleteActivities() #Returns the activities of an athlete. [{"resource_state : 2, "athlete : {"id" : 1234}, "id" : 123456}]
    print(em)

    print(" ")
    print("3. Get ActivityById: ")
    print(" ")
    print(stravaApiKud.getActivietesById(em[0]["id"]))
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

        datos = (aktibitatea["id"], aktibitatea['type'], data, kilometroak, denbora, ordua, atletaInfo['id'])
        if DatuBasea.entrenamenduaDagoenKonprobatu(aktibitatea["id"]) == 0:
            DatuBasea.EntrenamenduaSartu(datos)

        if aktibitatea['has_heartrate'] is False:
            aktibitatea['average_heartrate'] = 0.0

        print("Posizioa", aktibitatea['start_latlng'])
        print("Abiadura", aktibitatea['average_speed'])
        print("pultsazioak", aktibitatea['average_heartrate'])
        print("entreData", data)
        print("entreOrdua", ordua)
        print("idEntrenamendua", aktibitatea["id"])
        latilng=' '.join(str(e) for e in aktibitatea['start_latlng'])


        medizioak = (latilng, aktibitatea['average_speed'], aktibitatea['average_heartrate'], data, ordua, aktibitatea["id"])
        if DatuBasea.medizioakDagoenKonprobatu(aktibitatea["id"]):
            DatuBasea.medizioakSartu(medizioak)

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