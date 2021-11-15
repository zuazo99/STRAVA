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
    print("1. Get AthleteActivities: ")
    print(" ")
    print(stravaApiKud.getAthleteActivities())
    print(" ")
    print("1. Get ActivityById: ")
    print(" ")
    print(stravaApiKud.getActivietesById())
    print(" ")
    print("1. Get ActivityStreams: ")
    print(" ")
    print(stravaApiKud.getActivityStreams())
