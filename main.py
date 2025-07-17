import requests
import time
import datetime

while True:
    response = requests.get('https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard')
    data = response.json() if response and response.status_code == 200 else None

    now = datetime.datetime.now()
    now = datetime.datetime(2025, 9, 4) # comment this line when you're done testing or change the date to simulate game days

    today_games = []

    # compile a list of today's games
    for event in (data.get('events')):
        gametime = event['competitions'][0]['status']['type']['shortDetail'].replace('/', " ").split(" ")
        if int(gametime[0]) == int(now.strftime("%m")) and int(gametime[1]) == int(now.strftime("%d")):
            today_games.append(event)
    # for x in today_games:
    #     print(x)

    if len(today_games) > 0:
        for event in today_games:
            for comp in (event['competitions']):
                competitors = comp['competitors']

                if comp['status']['type']['state'] == "pre":
                    gametime = event['competitions'][0]['status']['type']['shortDetail'].replace('/', " ").split(" ")
                    print(f"Starts @ {gametime[3]}{gametime[4]} {gametime[5]}")
                elif comp['status']['type']['state'] == "inprogress": # change to proper once you figure it out
                    print(f"Q{comp['status']['period']} {comp['status']['clock']} / {comp['status']['displayClock']}")

                # print(f"Odds: {comp['odds'][0]}")

                if comp['odds'][0]['awayTeamOdds']['favorite']:
                    fav = "away"
                else:
                    fav = "home"

                for team in competitors:
                    if team['homeAway'] == "home":
                        loc = "(H)"
                        if fav == "home":
                            loc += "*"
                    else:
                        loc = "(A)"
                        if fav == "away":
                            loc += "*"

                    if comp['status']['type']['completed']: #game is over
                        status = "FINAL"
                    else:
                        status = ""
                    print(f"{team['team']['shortDisplayName']} {loc} ({team['records'][0]['summary']}) --> {team['score']}")
                    # print(team['team']['logo']) # graphics URL
                print(status)
                # print('\n')

                if competitors[0]['team']['shortDisplayName'] == "Bears" or competitors[1]['team']['shortDisplayName'] == "Bears":
                    time.sleep(30) # pause longer on the bears when they are playing
                else:
                    time.sleep(5) # all other teams delay
    else:
            print("No Game Today --> spend time with your family instead")
            time.sleep(60*60)
