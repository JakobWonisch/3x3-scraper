import requests

def insertValue(s, k, v):
    return s.replace("{{" + k + "}}", v)

def getText(url):
    html_text = requests.get(url).text
    # unescaped = html_text.encode("utf-8").decode('unicode_escape')
    # print(html_text)
    # return unescaped.replace("\/", "/")
    return html_text.replace("\/", "/").replace("\\n", "\n").replace("\\\"", "\"")

def parseShots(s):
    if s == "":
        return (0, 0)
    
    parts = s.split("/")

    return (float(parts[0]), float(parts[1]))

def parseMinutes(s):
    if s == "":
        return 0
    
    parts = s.split(":")

    return int(parts[0]) + int(parts[1]) / 60