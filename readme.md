# 3x3 Scraper

This is a series of python scripts for scraping fiba3x3 play-by-play data of World Tour games.

Basic scraped data (list of events and games) can be found in the [output](/output) directory.
Full scraped data ([playbyplay + stats](https://hierwonisch.at/downloads/3x3scraper/playbyplay_and_stats.json), [playbyplay only](https://hierwonisch.at/downloads/3x3scraper/playbyplay.json) and [stats only](https://hierwonisch.at/downloads/3x3scraper/stats.json)) can be downloaded by clicking on the links, since they are too large for GitHub.

The structure of the json files is documented in the corresponding .structure.json file.
The playbyplay and stats trees are just downloads of the fiba3x3 api so their structure can easily be viewed in a browser at these randomly picked example links: [playbyplay](https://worldtour.fiba3x3.com/api/v2/game/27ab4f72-3055-4749-a54f-e8829bc6a957/playbyplay/scoring) and [stats](https://worldtour.fiba3x3.com/api/v2/game/27ab4f72-3055-4749-a54f-e8829bc6a957/stats)
These json files have been printed without indentation to minimize file size. If you want to make them easier to read download them into the output directory and run `python json_prettify.py` in the root directory of the repository (the same directory this readme file is in).
