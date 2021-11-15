from controllers.StravaAPI import stravaApiKud
# kaixo


if __name__ == '__main__':
    stravaApiKud.getAccessToTheAPI()
    print(stravaApiKud.getAthlete())
    print(stravaApiKud.getAthleteActivities())
    print(stravaApiKud.getActivietesById())
    print(stravaApiKud.getActivityStreams())
