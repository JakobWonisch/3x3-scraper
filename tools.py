import requests

def insertValue(s, k, v):
    if type(k) is not list:
        k = [ k ]
        v = [ v ]
    
    res = s

    i = 0
    for key in k:
        res = res.replace("{{" + key + "}}", v[i])
        i = i + 1

    return res

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