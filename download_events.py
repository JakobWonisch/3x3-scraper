from constants import *
from tools import *
import json
import re

# all data will be collected in this array
data = {}

for season in range(2012, 2022):
    print("processing season " + str(season))
    url = insertValue(query_events, "season", str(season))
    text = getText(url)

    matches = re.findall(re_events, text)
    year = []
    for m in matches:
        if m in generic_links:
            continue

        year.append(m)
    
    year = list(dict.fromkeys(year))
    data[str(season)] = year


# write data to file
with open("output/events.json", "w") as outfile:
    json.dump(data, outfile, indent = 4)