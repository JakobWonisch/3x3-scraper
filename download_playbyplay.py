from constants import *
from tools import *
import json
import re


# load events
with open("output/games.json", "r") as outfile:
    games = json.load(outfile)

# all data will be collected in this array
data = {}

for seasonI in range(2022, 2011, -1):
    season = str(seasonI)
    year = {}
    for event in games[season]:
        eventList = {}
        for game in games[season][event]:
            print(f"processing game {game} at {event} in {season}")
            urlPlaybyplay = insertValue(query_playbyplay, "game", game)
            urlStats = insertValue(query_stats, "game", game)
            eventList[game] = {
                "playbyplay": getJson(urlPlaybyplay),
                "stats": getJson(urlStats)
            }
        year[event] = eventList
        data[season] = year
    
        # write data to file
        with open("output/playbyplay.json", "w") as outfile:
            json.dump(data, outfile, indent = 4)

    
