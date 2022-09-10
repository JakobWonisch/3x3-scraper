from constants import *
from tools import *
import json
import re


# load events
with open("output/events.json", "r") as outfile:
    events = json.load(outfile)

# all data will be collected in this array
data = {}

for season in events:
    year = {}
    for event in events[season]:
        print("processing event " + event + ", " + season)
        url = insertValue(query_games, [ "season", "event" ], [ season, event ])
        text = getText(url)

        matches = re.findall(re_games, text)
        eventList = []
        for m in matches:
            if m in generic_links:
                continue

            eventList.append(m)
        year[event] = eventList
        
    data[season] = year

    # write data to file
    with open("output/games.json", "w") as outfile:
        json.dump(data, outfile, indent = 4)
