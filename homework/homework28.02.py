'''
Следующее задание такое.

Нужно выбрать для себя новостной сайт.
Заведите себе гуглдок и запишите туда свои сайты -- чтобы не повторяться.

В репозитории должен лежать готовый код, который умеет делать всё, что я перечислю ниже, а также в файле Readme.md в папке с проектом должна находиться ссылка на скачанные и обработанные файлы вашего новостного сайта, лежащие архивом на Яндекс.Диске, Google Drive, Облаке@Мэйл.ру или на чём угодно подобном.
При этом
1. Период, за который должны быть тексты: 1 июля 2015 -- 31 декабря 2018 года.
2. Общий объём скачанных текстов должен быть не меньше 5 млн. слов (можно больше).
3. В именах файлов не должно быть не-ascii символов.
4. Структура каталогов, в которых хранятся файлы, должна быть следующей: корень/год/месяц/файлы с материалами за этот месяц
5. В корне также должна лежать csv-таблица с полями, которые я перечислю ниже.

Соответственно, сама программа (в одном или в нескольких файлах) должна уметь:
1. написать программу, которая умеет автоматически обращаться к сайту газеты и скачивать оттуда html-страницы, при этом программа должна уметь находить ссылки на другие страницы этого сайта и скачивать их тоже.
При этом программа не должна заходить на одни и те же страницы несколько раз.
2. с помощью lxml (или другого парсера xml) извлекать со страниц информацию (если она доступна) для метатаблицы и сам текст.
Метатаблица должна иметь следующие поля:
path;author;date;source;title;url;wordcount
path -- это путь к файлу.
source -- это название новостного сайта.
wordcount -- число слов в тексте.
Остальное, думаю, понятно (если вдруг непонятно, пишите).
3. раскладывать скачанные тексты по папкам (в соответствии с теми правилами, которые изложены выше).
4. вызывать mystem и делать морфологическую разметку текста (таким образом, чтобы каждому слову была присвоена информация о лемме и грамматическая информация с учётом контекстно снятой омонимии).
Размеченные майстемом файлы должны лежать в отдельной папке. То есть структура каталога должна быть такая:

корень
|
|___ plain text
|      |___год
|            |___месяц
|___ размеченные майстемом тексты
       |___год
             |___месяц
Файлы, размеченные майстемом, записывать в метатаблицу не надо.

Сделать всё нужно до 23:59 28 февраля 2019 года.
'''

# vedomosti.ru/*/articles/year/month/day/name
from lxml import html
import urllib.request
from datetime import datetime
from string import punctuation
import os
from pymystem3 import Mystem
import re
import json

def access_site(url):
    doc = urllib.request.urlopen(url)
    content = doc.read().decode("utf-8")
    tree = html.fromstring(content)
    return tree


def link_getter(tree):
    linkslist = []
    links = tree.xpath('.//div[@class="b-article__title"]/a')
    for link in links:
        newurl = link.attrib["href"]
        if re.search("articles", newurl) is not None:
            linkslist.append(newurl)
    return linkslist


def tag_extraction(tree):
    #  TITLE catching
    title = tree.xpath('.//h1[@class="title"]')[0].text_content()
    title = title.rstrip("\n").rstrip().lstrip().lstrip("\n")
    titlepath = re.sub("([/?!*\"><|\\\\])", "", title)
    #  AUTHOR catching
    try:
        authors = tree.xpath('.//div[@class="b-document__authors"]/ul/li/a')
        authorslist = []
        for singauthor in authors:
            authorslist.append(singauthor.text_content())
        author = " ".join(authorslist)
    except:
        author = ""
    #  SOURCE catching
    try:
        source = tree.xpath('.//div[@class="b-document__authors"]/ul/li[@class="b-document__authority"]/a')[0].text_content()
    except:
        source = ""

    return title, titlepath, author, source


def text_extractor(tree):
    articletext = []
    texts = tree.xpath('.//div[@class="b-document__body b-social__layout-mutation"]/p')
    for text in texts:
        paragraph = text.text_content()
        paragraph = paragraph.rstrip("\n").rstrip().lstrip().lstrip("\n")
        articletext.append(paragraph)
    articletext = " ".join(articletext)
    wordcount = len([word.strip(punctuation+'«»—…“”*№–') for word in articletext.lower().split()])
    return articletext, wordcount

def csv_updater(file, path, title, date, author, source, url, wordcount):
    with open(file, "a", encoding="utf-8") as w:
        w.write(path + "\t" + author + "\t" + date + "\t" + source + "\t" + title + "\t" + url + "\t" + str(wordcount) + "\n")
        w.close()

def text_writer(text, path):
    with open(path, "w+", encoding="utf-8") as w:
        w.write(text)


def my_stemmer(text):
    m = Mystem()
    analyzedtext = m.analyze(text)
    return analyzedtext


if __name__ == "__main__":
    # 1 июля 2015 -- 31 декабря 2018
    basefolder = r"D:/homework280219"
    csv = basefolder + "/filetable.csv"
    folderplain = basefolder + "/plain_text"
    folderstem = basefolder + "/mystem_text"
    os.mkdir(basefolder)
    f = open(csv, "w+")
    f.close()
    os.mkdir(folderplain)
    os.mkdir(folderstem)
    url = "https://www.vedomosti.ru/archive"
    for year in range(2015, 2018+1):
        os.mkdir(folderplain + "/" + str(year))
        os.mkdir(folderstem + "/" + str(year))
        for month in range(1, 12+1):
            os.mkdir(folderplain + "/" + str(year) + "/" + str(month))
            os.mkdir(folderstem + "/" + str(year) + "/" + str(month))
            for day in range(1, 31+1):
                try:
                    datetime(year, month, day)
                    datevalid = True
                except:
                    datevalid = False
                if datevalid is True and datetime(year, month, day) >= datetime(2015, 7, 1):
                    daylinks = link_getter(access_site(url + "/" + str(year) + "/" + str(month) + "/" + str(day)))
                    for daylink in daylinks:
                        dayurl = "https://www.vedomosti.ru" + daylink
                        date = str(year) + "/" + str(month) + "/" + str(day)
                        tree = access_site(dayurl)
                        title, titlepath, author, source = tag_extraction(tree)
                        text, wordcount = text_extractor(tree)
                        path = folderplain + "/" + str(year) + "/" + str(month) + "/" + titlepath + ".txt"
                        stemmedpath = folderstem + "/" + str(year) + "/" + str(month) + "/" + titlepath + ".txt"
                        text_writer(text, path)
                        csv_updater(csv, path, title, date, author, source, dayurl, wordcount)
                        stemmedtext = my_stemmer(text)
                        text_writer(json.dumps(stemmedtext), stemmedpath)
