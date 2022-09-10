from constants import *
from tools import *
import json
from concurrent.futures import ThreadPoolExecutor, as_completed


# load events
with open("output/games.json", "r") as outfile:
    games = json.load(outfile)

# all data will be collected in this array
data = {}

def downloadJson(game, event, season):
    # print(f"processing game {game} at {event} in {season}")
    urlPlaybyplay = insertValue(query_playbyplay, "game", game)
    urlStats = insertValue(query_stats, "game", game)
    return {
                "game": game,
                "event": event,
                "season": season,
                "playbyplay": getJson(urlPlaybyplay),
                "stats": getJson(urlStats)
            }

pool = ThreadPoolExecutor(max_workers=40)
futures = []

for seasonI in range(2022, 2011, -1):
    season = str(seasonI)
    for event in games[season]:
        for game in games[season][event]:
            futures.append(pool.submit(downloadJson, game, event, season))
    
nLoaded = 0
for future in as_completed(futures):
    result = future.result()

    season = result["season"]
    event = result["event"]
    game = result["game"]

    if season not in data:
        data[season] = {}
    if event not in data[season]:
        data[season][event] = {}

    data[season][event][game] = {
        "playbyplay": result["playbyplay"],
        "stats": result["stats"]
    }

    nLoaded = nLoaded + 1
    print(f"{nLoaded} loaded {game} at {event} in {season}")

    if nLoaded % 250 == 0:
        # write data to file
        with open("output/playbyplay.json", "w") as outfile:
            json.dump(data, outfile, indent = 4)

pool.shutdown()
