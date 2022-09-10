from constants import *
from tools import *
import json

# load
print("processing playbyplay...")
with open("output/playbyplay_and_stats.json", "r") as outfile:
    playbyplay = json.load(outfile)

for season in playbyplay:
    for event in playbyplay[season]:
        for game in playbyplay[season][event]:
            del playbyplay[season][event][game]["stats"]

with open("output/playbyplay.json", "w") as outfile:
    json.dump(playbyplay, outfile)
    # json.dump(playbyplay, outfile, indent = 4)

print("processing stats...")
with open("output/playbyplay_and_stats.json", "r") as outfile:
    stats = json.load(outfile)
    
for season in stats:
    for event in stats[season]:
        for game in stats[season][event]:
            del stats[season][event][game]["playbyplay"]

with open("output/stats.json", "w") as outfile:
    json.dump(stats, outfile)
    # json.dump(stats, outfile, indent = 4)

print("done.")