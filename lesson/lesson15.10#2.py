#open text file with china space program, find all china space apparatus names and add in list (only CHINA)

import re
with open("chinakp.txt", "r", encoding="utf-8") as r:
    f = r.read()
    y = re.findall("«.+?[0-9]»", f)
    s = re.findall("«[ЮДШТЧ].+?[унэ]-*[0-9]*»", f)