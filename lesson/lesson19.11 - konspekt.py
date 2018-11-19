# text mining

import re
import urllib.request
import html
import time

doc = urllib.request.urlopen("https://hse.ru")
content = doc.read().decode("utf-8")  # .read reads in ascii
print(doc.info())  # info about the site

# some site block python requests to obtain data, how to make us look like normal users?
# check in internet which formulas can be inserted
user_agent = "Mozilla/5.0..."
req = urllib.request.Request("https://hse.ru", headers={"User-Agent": user_agent})
doc = urllib.request.urlopen(req)
content = doc.read().decode("utf-8")
title = re.search("<title>(.+?)</title>", content)
# & means in html has special meaning = &amp; &nbsp; etc...
s = "&nbsp;"
s = html.unescape(s)
time.sleep(2)  # makes the program wait for 2 seconds