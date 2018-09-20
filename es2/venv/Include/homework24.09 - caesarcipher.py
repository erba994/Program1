alphabet = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и",
            "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
            "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь",
            "э", "ю", "я")
cipher = alphabet[1:] + alphabet[:1]

cleancaesar = input("напишите предложение: ").split(" ")
cleancaesar = cleancaesar[:-2]+cleancaesar[:-3:-1]
caesar = " ".join(cleancaesar)
for letter in caesar:
    if letter in alphabet:
        print(cipher[alphabet.index(letter)], end="")
    else:
        print(letter, end="")

