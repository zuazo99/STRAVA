from controllers import DBKud
from controllers.StravaAPI import stravaApiKud
from controllers import DBKud
# kaixo


if __name__ == '__main__':
    print(" ")
    print("Konexioa egiten APIarekin: ")
    print(" ")

    #print("Datu basea proba:")
    #DBKud.datuBaseKud()


    stravaApiKud.getAccessToTheAPI()
    print(" ")
    print("1. Get Athlete: ")
    print(" ")
    print(stravaApiKud.getAthlete())
    print(" ")
    print("2. Get AthleteActivities: ")
    print(" ")
    em = stravaApiKud.getAthleteActivities()
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
        for e in aktibitateInfo:
            d = aktibitateInfo[e]["data"]
            luzera = len(d)
            for segundua in range(luzera-1):
                print(e, d[segundua])
                # Hemen joango zen SQL Insert-a
        print(" --- ")
        print(" ")
