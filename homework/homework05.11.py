import re
import os


def get_files_list(path):
    filelist = []
    directory = os.listdir(path)
    for file in directory:
        filelist.append(file)
    return filelist


def read_file(path, filename):
    with open(path + os.sep + filename, "r", encoding="utf-8") as r:
        text = r.read()
        return text


def sub_text(text, filename):
    if filename == "лингвистика.txt":
        text = re.sub("\\bязык(а|у|ом|е|и|ов|ам|ами|ах)?\\b", "шашлык\\1", text)
        text = re.sub("\\bЯзык(а|у|ом|е|и|ов|ам|ами|ах)?\\b", "Шашлык\\1", text)
        text = re.sub("\\bЯЗЫК(А|У|ОМ|Е|И|ОВ|АМ|АМИ|АХ)?\\b", "ШАШЛЫК\\1", text)
    if filename == "философия.txt":
        text = re.sub("\\bфилософи(я|и|ю|ей|й|ям|ями|ях)?\\b", "астрологи\\1", text)
        text = re.sub("\\bФилософи(я|и|ю|ей|й|ям|ями|ях)?\\b", "Астрологи\\1", text)
        text = re.sub("\\bФИЛОСОФИ(Я|И|Ю|ЕЙ|Й|ЯМ|ЯМИ|ЯХ)?\\b", "АСТРОЛОГИ\\1", text)
    if filename == "финляндия.txt":
        text = re.sub("\\bфинлянди(я|и|ю|ей)?\\b", "малайзи\\1", text)
        text = re.sub("\\bФинлянди(я|и|ю|ей)?\\b", "Малайзи\\1", text)
        text = re.sub("\\bФИНЛЯНДИ(Я|И|Ю|ЕЙ)?\\b", "МАЛАЙЗИ\\1", text)
    return text


def save_file(text, filename):
    with open("homework05.11" + os.sep + "newarticles" + os.sep + filename, "w+", encoding="utf-8") as r:
        r.write(text)


if __name__ == "__main__":
    filelist = get_files_list("homework05.11")
    os.mkdir("homework05.11" + os.sep + "newarticles")
    for filename in filelist:
        article = read_file("homework05.11", filename)
        article = sub_text(article, filename)
        save_file(article, filename)
