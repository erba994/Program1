# start from address, work text and obtain links to other webpages, repeat the procedure for every accessed page

import re
import urllib.request
import html


def get_that_webpage(internetpage):
    doc = urllib.request.urlopen(internetpage)
    content = doc.read().decode("utf-8")
    return content


def get_those_links(htmlpage):
    links = re.findall("<a href =\"(.+?)\".+?>", htmlpage)
    links = set(links)
    newlinks = []
    for link in links:
        link = re.sub("^(.+?)/servizi", "http://museomarineria.comune.cesenatico.fc.it/servizi", link)
        newlinks.append(link)
    return newlinks


def page_parsing(htmlpage):
    title = re.findall("<h1>(.+?)</h1>", htmlpage)
    n = 0
    for element in title:
        element = re.sub("<.+?>", "", element)
        element = html.unescape(element)
        title[n] = element
        n += 1
    text = re.findall("<p>(.+?)</p>", htmlpage)
    n = 0
    for part in text:
        part = html.unescape(part)
        text[n] = part
        n += 1
    article = "\n".join(title) + "\n" + "\n".join(text)
    return article


def walk_the_site(url):
    page = get_that_webpage(url)
    links = get_those_links(page)
    article = page_parsing(page)
    return links, article


if __name__ == "__main__":
    url = "http://museomarineria.comune.cesenatico.fc.it/servizi/notizie/notizie_homepage.aspx"
    visitedarticles = []
    visitedlinks = []
    links, article = walk_the_site(url)
    visitedarticles.append(article)
    for link in links:
        if link not in visitedlinks:
            newlinks, article = walk_the_site(link)


