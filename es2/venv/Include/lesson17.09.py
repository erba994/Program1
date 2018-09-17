while True:
    s = input('напишите предложение: ')
    s = s.split()
    for word in s:
        word = word.strip(".,!?:;-_\"+").lower()
        if len(word) >= 3:
            if word.endswith("и" or "ы"):
                print(word, " - существительное, мужской или женский род, множественное число")
            elif word.endswith("а" or "я"):
                print(word, " - существительное, женский род и единственное число или средний род и множественное число")
            elif word.endswith("о" or "е"):
                print(word, " - существительное, средний род и единственное число или наречие")
            elif word.endswith("ность"):
                print(word, " - существительное, женский род и единственное число")
            elif word.endswith("ать" or "ить"):
                print(word, " - глагол")
            elif word.endswith("ый" or "ий" or "ой"):
                print(word, " - прилагательное, мужской род и единственное число")
            elif word.endswith("ая" or "яя"):
                print(word, " - прилагательное, женский род и единственное число")
            elif word.endswith("ое" or "ее"):
                print(word, " - прилагательное, средний род и единственное число")
            elif word.endswith("ые" or "ие"):
                print(word, " - прилагательное, множественное число")
            elif word.endswith("ь"):
                print(word, " - существительное, мужской или женский род, единственное число")
            else:
                print(word, " - существительное, мужской род и единственное число")
        else:
            if len(word) > 0:
                print(word, " - не могу угадать")
            else:
                break