import random
import string


def generuj(n, x):

    wygenerowana_lista = []

    for _ in range(n):
        wyraz = ''
        for _ in range(random.randint(1,x)):
            wyraz += random.choice(string.ascii_lowercase)
        wygenerowana_lista.append(wyraz)
    return  wygenerowana_lista

n = int(input("ile elementow"))
x = int(input("podaj dlugosc elementow"))
krotka = tuple(generuj(n,x))

print(krotka)
dlugosc = 0
for v in krotka:
   dlugosc+=len(v)
print(dlugosc,"ilosc znakow")
dlugosc = 0
for v in krotka:
   dlugosc+=v.count('k')
print(dlugosc,"ilosc liter k")
dlugosc = 0
for v in krotka:
   dlugosc+=v.count('kt')
print(dlugosc,"ilosc  kt")

s = int(input("podaj s"))
for v in krotka:
    if len(v)> s:
        dlugosc += 1

print(dlugosc,"ilosc ciagow dluzszych niz s")