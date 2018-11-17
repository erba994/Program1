import os
import re
origin = "pirandelloor.txt"
os.mkdir(origin + " re")
with open(origin, "r", encoding="latin-1") as r:
    opera = r.readlines()
    print(opera)
    atto = []
    element = ""
    for line in opera:
        if re.search("A T T O", line):
            atto.append(element)
            element = line
        else:
            element += line
    atto.append(element)
    atto.pop(0)
    for n in range(len(atto)):
        os.mkdir(origin + " re" + os.sep + "atto" + str(n))