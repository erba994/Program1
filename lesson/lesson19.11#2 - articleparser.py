# сми download article and obtain text, write into file

import re
import urllib.request

doc = urllib.request.urlopen("https://www.kommersant.ru/doc/3800346")
print(doc.info())
content = doc.read().decode("windows-1251")
title = re.findall("<title>(.+?)</title>", content)
text = re.findall("<p class=\"b-article__text\">(.+?)</p>", content)
with open("lesson19.11#2.txt", "w+", encoding="windows-1251") as f:
    f.write(title[0] + "\n")
    for row in text:
        row = re.sub("<(.+?)>", "", row)
        f.write(row)


