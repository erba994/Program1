d = {"а": "а", "б": "b", "в": "v", "г": "g", "д": "d",
     "е": "e", "ё": "e", "ж": "zh", "з": "z", "и": "i",
     "й": "iy", "к": "k", "л": "l", "м": "m", "н": "n",
     "о": "o", "п": "p", "с": "s", "т": "t", "у": "u",
     "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh",
     "щ": "shch", "ъ": "'", "ы": "y", "ь": "'", "э": "e",
     "ю": "ju", "я": "ya"}

a = input("напишите слово: ")
for letter in a:
    if letter in d:
        print(d[letter], end="")
    else:
        print(letter, end="")