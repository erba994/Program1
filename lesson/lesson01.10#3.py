#читать файл, вводят в нижний регистр, разделяет слова, убирает снаки препинаниа, печатает пословно

def open_file(filename):
    f = open(filename, "r", encoding="utf-8")
    s = f.readlines()
    s = "".join(s)
    f.close()
    return s

def punctuation_clean(s):
    l = []
    for word in s:
        l.append(word.strip(".(),;:-_!?"))
    return l

def word_clean(s):
    f = s.split()
    return f

f = open_file("bello.txt")
f = word_clean(f)
f = punctuation_clean(f)
print(" ".join(f))