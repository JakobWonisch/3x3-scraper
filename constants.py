
query_events = "https://worldtour.fiba3x3.com/{{season}}/"
query_games = "https://worldtour.fiba3x3.com/{{season}}/{{event}}/games"
query_playbyplay = "https://worldtour.fiba3x3.com/api/v2/game/{{game}}/playbyplay/scoring"
query_stats = "https://worldtour.fiba3x3.com/api/v2/game/{{game}}/stats"

generic_links = [
    "teams",
    "standings",
    "news",
    "photos",
    "videos",
    "how-to-qualify",
    "more",
    "challengers",
    "stats",
    "calendar",
    "where-to-watch",
    "superquests"
]

re_events = r"<a href=\"/[0-9]*?/([^/\"]+?)\""
re_games = r"href=\"/[0-9]*?/[^/\"]+?/games/([^/\"]+?)\""