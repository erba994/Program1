# parse text from social networks or SMI, create a corpus with more than a million words (for smi) or 10.000 (for vk), and lemmatize them, put data and author (and more info if social network). Number refers to token analysed. every text to analyze and analyzed should be in a single .txt file in a single folder. received file needs to be a tsv with the list of analyzed files (path, author, (possible added fields), title, date, url)

import urllib.request
import json
from pymystem3 import Mystem


def vk_json_parser(accesstoken, counter):
    url = "https://api.vk.com/method/wall.get?owner_id=" + str(counter) + "&count=1&v=5.9&access_token=" + str(accesstoken)
    doc = urllib.request.urlopen(url)
    content = doc.read().decode("utf-8")
    counter += 1
    return content, counter


def get_that_json(jsonobject):
    data = json.loads(jsonobject)
    if data["response"] is not None:
        if len(data["response"]["items"][0]["text"]) > 0:
            text = data["response"]["items"][0]["text"]
            date = data["response"]["items"][0]["date"]
            likes = data["response"]["items"][0]["likes"]["count"]
            comments = data["response"]["items"][0]["comments"]["count"]
            reposts = data["response"]["items"][0]["reposts"]["count"]
    return text, (date, likes, comments, reposts)


def analyze_text(text):
    m = Mystem(mystem_bin=r"D:\loren\OneDrive\Documenti\Program\mystem.exe")
    txt = text
    ana = m.analyze(txt)
    return ana

def clean_stems():
    for word in list:
        for element in word:
            if "text" in element:
                write


if __name__ == "__main__":
    token = input(str("Enter your access token: "))
