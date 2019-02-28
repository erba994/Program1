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

def access_site(url):
    doc = urllib.request.urlopen(url)
    content = doc.read().decode("utf-8")
    tree = html.fromstring(content)
    return tree


def link_getter(tree):
    linkslist = []
    links = tree.xpath('.//div[@class="b-article__title"]/a')
    for link in links:
        linkslist.append(link.attrib["href"])
    return linkslist


def tag_extraction(tree):
    #  TITLE catching
    try:
        title = tree.xpath('.//h1[@class="title"]')[0].text_content()
        title = title.rstrip("\n").rstrip().lstrip().lstrip("\n")
    except:
        title = tree.xpath('.//div[@class="b-news-item__title b-news-item__title_one"]/h1')[0].text_content()
        title = title.rstrip("\n").rstrip().lstrip().lstrip("\n")
    #  AUTHOR catching
    try:
        author = tree.xpath('.//div[@class="b-document__authors"]/ul/li/a')[0].text_content()
    except:
        try:
            author = tree.xpath('.//a[@class="link b-document__authors decorate__border--right"]')[
                0].text_content()
        except:
            author = ""
    #  SOURCE catching
    try:
        source = tree.xpath('.//div[@class="b-document__authors"]/ul/li[@class="b-document__authority"]/a')[0].text_content()
    except:
        try:
            source = tree.xpath('.//a[@class="link b-document__authority decorate__border--right"]')[
                0].text_content()
        except:
            source = ""

    return title, author, source


def text_extractor(tree):
    articletext = []
    try:
        texts = tree.xpath('.//div[@class="b-document__body b-social__layout-mutation"]/p')
    except:
        node = tree.xpath('.//div[@class="b-news_wrapper b-news_wrapper-first"]/div/div/article')
        texts = node[0].xpath('./div/div/p')
    for text in texts:
        paragraph = text.text_content()
        paragraph = paragraph.rstrip("\n").rstrip().lstrip().lstrip("\n")
        articletext.append(paragraph)
    articletext = " ".join(articletext)
    wordcount = len([word.strip(punctuation+'«»—…“”*№–') for word in articletext.lower().split()])
    return articletext, wordcount

def csv_updater(file, path, title, date, author, source, url, wordcount):
    with open(file, "a", encoding="utf-8") as w:
        w.write(path + ", " + author + ", " + date + ", "+ source + ", " + title + ", " + url + ", " + wordcount + "\n")
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
    csv = "homework280219/filetable.csv"
    folderplain = "homework280219/plain_text"
    folderstem = "homework280219/mystem_text"
    if not os.path.exists("homework280219"):
        os.mkdir("homework280219")
    f = open(csv, "w+")
    f.close()
    os.mkdir("homework280219/plain_text")
    os.mkdir("homework280219/mystem_text")
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
                        title, author, source = tag_extraction(tree)
                        text, wordcount = text_extractor(tree)
                        path = folderplain + "/" + str(year) + "/" + str(month) + "/" + title + ".txt"
                        stemmedpath = folderplain + "/" + str(year) + "/" + str(month) + "/" + title + ".txt"
                        text_writer(text, path)
                        csv_updater(csv, path, title, date, author, source, dayurl, wordcount)
                        stemmedtext = my_stemmer(text)
                        text_writer(stemmedtext, stemmedpath)
