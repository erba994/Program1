a1 = input("напишите слово: ")
a2 = enumerate(a1)
l1 = list()
for count,letter in a2:
    if count % 2 == 1 and letter != "а" and letter != "к":
        l1.append(letter)
print(l1)

l2 = list()
b1 = int(input("напишите число: "))
for number in range(b1):
    b2 = input("напишите слово: ")
    if b2 != ("программирование"):
        l2.append(b2)
    else:
        break
if len(l2) == b1:
    print(l2)