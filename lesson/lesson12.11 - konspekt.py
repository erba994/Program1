import os
lst = os.listdir("dir")
for fl in lst:
    os.system("\"mystem.exe\" {} tag-{} -id".format(fl, fl)) # format not dependent on datatype, fl is list elem not str

from pymystem3 import Mystem  # works automatically in POS disambiguation mode, slower than .exe
m = Mystem()
txt = "Мама мыла раму"
lemmas = m.lemmatize(txt)
ana = m.analyze(txt)  # list of dictionaries with a name and a list of dictionaries for analysis [{text, analysis:[{}}}]

import pymorphy2  # open source and Python native, OpenCorpora data, can generate forms not only analyze, no disambiguation
# choice between candidates it is worked from probability in whole corpus of one over the other
morph = pymorphy2.MorphAnalyzer()
p = morph.parse("маму")[0]
print(p.tag)
print(p.normal_form)

# n2: обработать один текст pymystem3 и pymorphy2, посчитать число совпадающих разборов дла этих инструментов
# (для pymorphy2 считать первую по счету разбор)