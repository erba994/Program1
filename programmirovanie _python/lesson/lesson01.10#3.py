#читать файл, вводят в нишнем регистре, разделит слова, выбирает снаки препинаниа печатать пословно

def open_file(filename):
    f = open(filename, "r", encoding="utf-8")
    s = f.readlines()
    f.close()
    return s

def punctuation_clean(s):
    for word in s:
        word.strip(".,;:-_!?")
        return s

def word_clean(s):
    s = s.split("")
    return s

f = open_file("bello.txt")
f = punctuation_clean(f)
f = word_clean(f)
print(f)