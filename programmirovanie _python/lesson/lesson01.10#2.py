#aprire, leggere, fare dizionario, chiave latino, valore amkarskij

f = open(r"C:\Users\Lorenzo Tosi\Program1\programmirovanie _python\lesson\amkarski.csv", "r", encoding="utf-8")
s = f.read()
f.close()
s = s.split("\t")
dict = {}
print(s)
