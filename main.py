import requests
import time
import datetime
import yfinance as yf

favourite_team = "Bears" # input favourite team and when they are playing show nothing else to rotate all teams

while True:
    response = requests.get('https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard')
    data = response.json() if response and response.status_code == 200 else None

    now = datetime.datetime.now()
    # now = datetime.datetime(2025, 9, 7) # comment this line when you're done testing or change the date to simulate game days

    today_games = []

    # compile a list of today's games
    for event in (data.get('events')):
        gametime = event['competitions'][0]['status']['type']['shortDetail'].replace('/', " ").split(" ")
        if int(gametime[0]) == int(now.strftime("%m")) and int(gametime[1]) == int(now.strftime("%d")):
            today_games.append(event)
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
            elif event['competitions'][0]['status']['type']['state'] != "pre" and (event['competitions'][0]['competitors'][0]['team']['shortDisplayName'] == favourite_team or event['competitions'][0]['competitors'][1]['team']['shortDisplayName'] == favourite_team):
                favourite_game.append(event)
            else:
                active_games.append(event)

        # no need to tie up time with pregames, focus on only the favorite team, otherwise if there's an active game on,
        # show it, if neither advertise the schedule
        if len(favourite_game) > 0:
            today_games = favourite_game
        elif len(active_games) > 0:
            today_games = active_games
        else:
            today_games = pre_games

    if len(today_games) > 0:
        for event in today_games:
            for comp in (event['competitions']):
                competitors = comp['competitors']

                if comp['status']['type']['state'] == "pre":
                    gametime = event['competitions'][0]['status']['type']['shortDetail'].replace('/', " ").split(" ")
                    print(f"Starts @ {gametime[3]}{gametime[4]} {gametime[5]}")
                else:
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
                        status = "FINAL\n"
                    else:
                        status = ""
                    print(f"{team['team']['shortDisplayName']} {loc} ({team['records'][0]['summary']}) --> {team['score']}")
                    # print(team['team']['logo']) # graphics URL
                print(status)

                if competitors[0]['team']['shortDisplayName'] == favourite_team or competitors[1]['team']['shortDisplayName'] == favourite_team:
                    time.sleep(15) # pause longer on the bears when they are playing

                time.sleep(5) # all other teams delay
    else:
        print("No Game Today")
        sleeping = 0
        delay = 5
        stocks = ['XEQT.TO', 'VIDY.TO', 'AC.TO', 'CCL', 'COST', 'CP.TO', 'CNR.TO', 'DOL.TO', 'ENB.TO', 'FTS.TO', 'PZA.TO', 'NVDA', 'RIVN', 'TSLA']
        while sleeping < 3600:
            for stock in stocks:
                print(f"{stock} {round(yf.Ticker(stock).info['regularMarketChangePercent'],2)}%")
                time.sleep(delay)
                sleeping += delay
