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

# AJAX  # Asincronous way of creating dinamyic content. Browser interprets Javascript and through XML data is exchanged with background requests to the server.
# API  # Application Prgogramming Interface, to access and update data from websites (and not only)
# DOM  # Content tree of a webpage
# lxml  # in language html, rules on how to write and order tags in websites
# xpath  # language to write and order websites

from lxml import html
tree = html.fromstring(content)  # builds the LXML tree for a site, can be feeded only to lxml functions
tree.xpath('.//div[@class="news"]/p')[0]  # looks for <div class="descr"> html tags, if element is there returns the element, otherwise None
tree.xpath()[0].text_content()  # returns text (if contained in the text tag, not guaranteed to work always)

from bs4 import BeautifulSoup
soup = BeautifulSoup(content, features="lxml")
text = soup.find("font", size=2)  # if we use class here, Python interprets it as its own class and it breaks
text = soup.findAll("div", {"class": "news"})[0]  # in this way we can extract a class from a div element and rework it

from requests_html import HTML
html = HTML(html=content)
h1 = html.find(".news").text

#  to parse from VK: open app through vk.com/apps?act=manage
#  api.vk.com/method/wall.get?owner_id=1&count=2&v=5.7&access_token=mytoken
#  where owner_id is the id of one user (check it in his page or links to his stf), count is number of posts
#  result is a JSON object , to rework it
import json
data = json.loads(result)  # to work with text lines, dict is returned
json.dump(data, f, ensure_ascii=False, indent=2)  # convert Python to JSON: indent->how indented txt should be included
data.load(f)  # to work with objects
