import json

files = [ "output/playbyplay_and_stats.json", "output/playbyplay.json", "output/stats.json" ]

for f in files:
    print(f"processing {f}...")
    
    with open(f, "r") as outfile:
        data = json.load(outfile)
    
    with open(f, "w") as outfile:
        json.dump(data, outfile)