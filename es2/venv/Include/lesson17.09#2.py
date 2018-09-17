d = {"а": "а", "б": "b", "в": "v", "г": "g", "д": "d",
     "е": "e", "ё": "e", "ж": "zh", "з": "z", "и": "i",
     "й": "iy", "к": "k", "л": "l", "м": "m"}

a = input("напишите слово: ")
a = a.split()
for letter in a:
    if letter in d:
        print(d[letter])
    else:
        print(letter)