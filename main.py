from controllers import DBKud
from controllers.StravaAPI import stravaApiKud
from controllers import DBKud
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
    # DBKud.datuBaseKud(atletaInfo['id'], atletaInfo['firstname'], atletaInfo['lastname'])
    #DBKud.DBKudeaketa.atletaSartu(atletaInfo['id'], atletaInfo['firstname'], atletaInfo['lastname'])
    print("Datu basea atleta kontsultatu:")
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
        indizea = indizea + 1
        print(" ")
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
