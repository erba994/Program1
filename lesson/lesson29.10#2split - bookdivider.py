import os
origin = input()
os.mkdir(origin + " dir")
with open(origin, "r", encoding="latin-1") as r:
    opera = r.read()
    opera = opera.split("A T T O")
    opera.pop(0)
    numatto = 1
    for atto in opera:
        os.mkdir(origin + " dir" + os.sep + "ATTO" + str(numatto))
        atto = atto.split("SCENA")
        if len(atto) > 1:
            newatto = "".join("A T T O" + atto[0] + "SCENA" + atto[1])
            atto.pop(0)
            atto.pop(0)
            atto.insert(0, newatto)
        numscena = 1
        for scena in atto:
            if not numscena == 1:
                scena = "SCENA" + scena
            file = open(origin + " dir" + os.sep + "ATTO" + str(numatto) + os.sep + "scena" + str(numscena) + ".txt", "w", encoding="latin-1")
            file.write(scena)
            numscena += 1
        numatto += 1
