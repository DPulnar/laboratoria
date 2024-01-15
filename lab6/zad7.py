import random

krotka = tuple()
a = int(input("podaj poczatek przedzialu"))
b = int(input("podaj koniec przedzialu"))
krotka = list()
for i in range(0,10):
    krotka.append(random.randint(a,b))
krotka = tuple(krotka)
print(krotka)
print("srednia", sum(krotka) / len(krotka))
