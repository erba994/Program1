import random


def noun_s():
    with open("14_10_nomi.tsv", "r", encoding="utf-8") as f:
        file = f.read()
        nome = file.split(", ")
    return random.choice(nome)


def article_s(n):
    if n.endswith("e"):
        if n.startswith("a"):
            nome = ("l\'" + n)
        else:
            nome = ("il" + " " + n)
    elif n.endswith("a"):
        nome = ("la" + " " + n)
    else:
        nome = ("il" + " " + n)
    return nome


def noun_p(n):
    if n.endswith("e"):
        nome = (n.strip("e") + "i")
    elif n.endswith("a"):
        nome = (n.strip("a") + "e")
    else:
        nome = (n.strip("o") + "i")
    return nome


def article_p(np):
    if np.endswith("i"):
        if np.startswith("a"):
            nome = ("gli" + " " + np)
        else:
            nome = ("i" + " " + np)
    else:
        nome = ("le" + " " + np)
    return nome


def verb():
    with open("14_10_verbi.tsv", "r", encoding="utf-8") as f:
        file = f.read()
        verbo = file.split(", ")
    return random.choice(verbo)


def verbimp():
    with open("14_10_verimp.tsv", "r", encoding="utf-8") as f:
        file = f.read()
        verbo = file.split(", ")
    return random.choice(verbo)


def verbcong():
    with open("14_10_vercong.tsv", "r", encoding="utf-8") as f:
        file = f.read()
        verbo = file.split(", ")
    return random.choice(verbo)


def verbcond():
    with open("14_10_vercond.tsv", "r", encoding="utf-8") as f:
        file = f.read()
        verbo = file.split(", ")
    return random.choice(verbo)


def adverb():
    with open("14_10_avverbi.tsv", "r", encoding="utf-8") as f:
        file = f.read()
        avverbo = file.split(", ")
    return random.choice(avverbo)


def prep(na):
    art = na.split()
    if art[0].startswith("l"):
        preposizione = ("a" + "l" + art[0] + " " + art[1])
    else:
        preposizione = ("a" + art[0] + " " + art[1])
    return (preposizione)


def affirmative():
    v = verb()
    if v == "pensa":
        sentence = (article_s(noun_s()) + " " + v + " " + prep(article_p(noun_p(noun_s()))) + " " + adverb() + ".")
    elif v == "corre":
        sentence = (article_s(noun_s()) + " " + v + " " + "verso" + " " + article_p(noun_p(noun_s())) + " " + adverb() + ".")
    else:
        sentence = (article_s(noun_s()) + " " + v + " " + article_p(noun_p(noun_s())) + " " + adverb() + ".")
    return sentence


def question():
    v = verb()
    if v == "pensa":
        sentence = (v + " " + article_s(noun_s()) + " " + prep(article_p(noun_p(noun_s()))) + " " + adverb() + "?")
    elif v == "corre":
        sentence = (v + " " + article_s(noun_s()) + " " + "verso" + " " + article_p(noun_p(noun_s())) + " " + adverb() + "?")
    else:
        sentence = (v + " " + article_s(noun_s()) + " " + article_p(noun_p(noun_s())) + " " + adverb() + "?")
    return sentence


def negative():
    v = verb()
    if v == "pensa":
        sentence = (article_s(noun_s()) + " " + v + " " + prep(article_p(noun_p(noun_s()))) + " " + adverb() + ".")
    elif v == "corre":
        sentence = (article_s(noun_s()) + " " + v + " " + "verso" + " " + article_p(noun_p(noun_s())) + " " + adverb() + ".")
    else:
        sentence = (article_s(noun_s()) + " " + v + " " + article_p(noun_p(noun_s())) + " " + adverb() + ".")
    return sentence


def order():
    v = verbimp()
    if v == "pensa" or v == "di\' qualcosa":
        sentence = (noun_s() + ", " + v + " " + prep(article_p(noun_p(noun_s()))) + " " + adverb() + "!")
    elif v == "corri" or v == "nuota":
        sentence = (noun_s() + ", " + v + " " + "verso" + " " + article_p(noun_p(noun_s())) + " " + adverb() + "!")
    else:
        sentence = (noun_s() + ", " + v + " " + article_p(noun_p(noun_s())) + " " + adverb() + "!")
    return sentence


def conditional():
    sentence = ("se" + " " + article_s(noun_s()) + " " + verbcong() + " " + adverb() + "," + " " + (article_p(noun_p(noun_s()))) + " " + verbcond() + " " + adverb() + ".")
    return sentence


def main():
    with open("14_10_sentences.txt", "a", encoding="utf-8") as f:
        sentences = [affirmative(), negative(), question(), order(), conditional()]
        f.write(random.choice(sentences).capitalize() + "\n")
    return 0


if __name__ == '__main__':
    main()