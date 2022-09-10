from constants import *
from tools import *
import json
import re


# load events
with open("output/events.json", "w") as outfile:
    events = json.load(outfile)

# all data will be collected in this array
data = {}

for season in events:
    for event in events[season]:
        print("processing event " + event + " " + season)
        url = insertValue(query_games, "season", season)
        url = insertValue(url, "event", event)
        text = getText(url)

        matches = re.findall(re_games, text)
        year = []
        for m in matches:
            if m in generic_links:
                continue

            year.append(m)
        
        year = list(dict.fromkeys(year))
        data[str(season)] = year


# write data to file
with open("output/games.json", "w") as outfile:
    json.dump(data, outfile, indent = 4)