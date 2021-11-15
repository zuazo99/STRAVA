from controllers.StravaAPI import stravaApiKud
# kaixo


if __name__ == '__main__':
    print(" ")
    print("Konexioa egiten APIarekin: ")
    print(" ")
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
    print(stravaApiKud.getActivityStreams(em[0]["id"]))
