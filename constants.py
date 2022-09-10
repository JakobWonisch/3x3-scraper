
query_events = "https://worldtour.fiba3x3.com/{{season}}/"
query_games = "https://worldtour.fiba3x3.com/{{season}}/{{event}}/games"

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
re_games = r"<a href=\"/[0-9]*?/([^/\"]+?)\""