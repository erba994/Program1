a1 = enumerate(input("напишите слово: "))
# create list to attach letters according to instructions
l1 = list()
# select letters and append them to empty list
for count, letter in a1:
    if count % 2 == 1 and letter != "а" and letter != "к":
        l1.append(letter)
print(l1)

l2 = list()
# avoids breaking program if float is provided, converting type into int
b1 = int(float(input("напишите число: ")))
# program breaks on low register only
for number in range(b1):
    b2 = input("напишите слово: ")
    if b2 != "программирование":
        l2.append(b2)
    else:
        break
# program prints words only if all the cycles were successfully ran
if len(l2) == b1:
    print(l2)

a3 = input("напишите слово: ")
b3 = (list(a3)[:int(len(a3)/2)])
c3 = (list(a3)[int(len(a3)/2):])
c3 = c3[::-1]
print("".join(b3) + "".join(c3))