# python venv:
# python3 -m venv myenv
# source myenv/bin/activate - install dependencies
# run without activation use python reference venv python (have to sudo in linux to get socket permissions for ping it seems)
# sudo /home/user/scripts/GameDisplay/myenv/bin/python3 /home/user/scripts/GameDisplay/main.py

import requests
import time
# import datetime
from datetime import datetime, UTC
import zoneinfo
import yfinance as yf
import wled

favourite_team = "Bears" # input favourite team and when they are playing show nothing else to rotate all teams
prev_game_data = []

while True:
    response = requests.get('https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard')
    data = response.json() if response and response.status_code == 200 else None

    now = datetime.now()
    # now = datetime(2025, 7, 31) # comment this line when you're done testing or change the date to simulate game days

    today_games = []

    # compile a list of today's games
    for event in (data.get('events')):
        gametime = datetime.strptime(event['competitions'][0]['date'], "%Y-%m-%dT%H:%MZ")
        gametime = datetime.fromisoformat(str(gametime)).replace(tzinfo=UTC).astimezone()
        # print(gametime)
        if gametime.strftime("%m") == now.strftime("%m") and gametime.strftime("%d") == now.strftime("%d"):
            today_games.append(event)

    # clear stale historical data
    found = 0
    for prev_event in prev_game_data:
        prev_gametime = datetime.strptime(prev_event['competitions'][0]['date'], "%Y-%m-%dT%H:%MZ")
        prev_gametime = datetime.fromisoformat(str(prev_gametime)).replace(tzinfo=UTC).astimezone()
        if prev_gametime.strftime("%m") == now.strftime("%m") and prev_gametime.strftime("%d") == now.strftime("%d"):
            found += 1

    if found == 0:
        prev_event = [] # if we're running for more than a day we need to clear this old data
    # for x in today_games:
    #     print(x)

    # process today's games looking for favourites and active games
    pre_games = []
    active_games = []
    favourite_game = []

    if len(today_games) > 0:
        for event in today_games:
            if event['competitions'][0]['status']['type']['state'] == "pre":
                pre_games.append(event)
            elif event['competitions'][0]['status']['type']['state'] != "pre" and event['competitions'][0]['status']['type']['state'] != "post" and (event['competitions'][0]['competitors'][0]['team']['shortDisplayName'] == favourite_team or event['competitions'][0]['competitors'][1]['team']['shortDisplayName'] == favourite_team):
                favourite_game.append(event)
            else: # this covers active and post games
                active_games.append(event)

        # no need to tie up time with pregames, focus on only the favorite team, otherwise if there's an active game on,
        # show it, if neither advertise the schedule
        if len(favourite_game) > 0:
            today_games = favourite_game
        elif len(active_games) > 0:
            today_games = active_games
        else:
            today_games = pre_games

        if prev_game_data == []:
            prev_game_data = today_games

    if len(today_games) > 0:
        for event in today_games:
            for comp in (event['competitions']):
                competitors = comp['competitors']

                if comp['status']['type']['state'] == "pre":
                    gametime = event['competitions'][0]['status']['type']['shortDetail'].replace('/', " ").split(" ")
                    print(f"Starts @ {gametime[3]}{gametime[4]} {gametime[5]}")
                else:
                    print(f"Q{comp['status']['period']} {comp['status']['clock']} / {comp['status']['displayClock']}")


                # if comp['odds'][0]['awayTeamOdds']['favorite']:
                #     fav = "away"
                # else:
                #     fav = "home"

                # for team in competitors:
                    # if team['homeAway'] == "home":
                    #     loc = "(H)"
                        # if fav == "home":
                        #     loc += "*"
                    # else:
                    #     loc = "(A)"
                        # if fav == "away":
                        #     loc += "*"


                    # print(f"{team['team']['abbreviation']} ({team['records'][0]['summary']}) --> {team['score']}")
                    # print(team['team']['logo']) # graphics URL
                print(comp['status']['period'])
                team1 = f"{competitors[0]['team']['abbreviation']}-{competitors[0]['score']}"
                team2 = f"{competitors[1]['team']['abbreviation']}-{competitors[1]['score']}"
                if comp['status']['type']['completed']: #game is over
                    status = {'x': 0,
                              'y': 28,
                              'val': "FINAL"}
                elif int(comp['status']['period']) == 1:
                    print("Q1")
                    status = {'x': 0,
                              'y': 29,
                              'val': "Q1"}
                elif int(comp['status']['period']) == 2:
                    print("Q2")
                    status = {'x': 0,
                              'y': 29,
                              'val': "Q2"}
                elif int(comp['status']['period']) == 3:
                    print("Q3")
                    status = {'x': 0,
                              'y': 29,
                              'val': "Q3"}
                elif int(comp['status']['period']) == 4:
                    print("Q4")
                    status = {'x': 0,
                              'y': 29,
                              'val': "Q4"}
                else:
                    print("Q?")
                    status = {'x': 0,
                              'y': 29,
                              'val': "OT"}

                if not comp['status']['type']['completed']:
                    #status = None
                    for prev_event in prev_game_data:
                        for prev_comp in (prev_event['competitions']):
                            for prev_competitors in prev_comp['competitors']:
                                if competitors[0]['team']['abbreviation'] == prev_competitors['team']['abbreviation']:
                                    print(f"{competitors[0]['team']['abbreviation']}")
                                    print(f"old {prev_competitors['score']} new {competitors[0]['score']}")
                                    if prev_competitors['score'] != competitors[0]['score']:
                                        wled.celebrate()
                                        prev_game_data = today_games
                                        team1 += "*"
                                elif competitors[1]['team']['abbreviation'] == prev_competitors['team']['abbreviation']:
                                    print(f"{competitors[1]['team']['abbreviation']} ")
                                    print(f"old {prev_competitors['score']} new {competitors[1]['score']}")
                                    if prev_competitors['score'] != competitors[1]['score']:
                                        wled.celebrate()
                                        prev_game_data = today_games
                                        team2 += "*"

                wled.static_wled_text(team1, team2,"555555","000000", status)

                # if competitors[0]['team']['abbreviation'] == favourite_team or competitors[1]['team']['abbreviation'] == favourite_team:
                #     time.sleep(15) # pause longer on the bears when they are playing

                time.sleep(15) # all other teams delay
    else:
        print("No Game Today")
        sleeping = 0
        delay = 5
        stocks = ['SPY', 'XEQT.TO', 'VIDY.TO', 'AC.TO', 'CCL', 'COST', 'CP.TO', 'CNR.TO', 'DOL.TO', 'ENB.TO', 'FTS.TO', 'PZA.TO', 'NVDA', 'RIVN', 'TSLA', 'BTC-CAD']
        while sleeping < 3600:
            text = ""
            pointer = 0
            while pointer < len(stocks):
                text1 = f"{stocks[pointer]}"
                text2 = f" {round(yf.Ticker(stocks[pointer]).info['regularMarketChangePercent'],2)}%"
                wled.static_wled_text(text1,text2,"555555","000000")
                pointer += 1
                time.sleep(delay)
                wled.celebrate()
            sleeping += delay
