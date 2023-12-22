import random
import string


def generuj(n, x):

    generated_strings = []

    for _ in range(n):
        current_string = ''
        for _ in range(random.randint(1,x)):
            current_string += random.choice(string.ascii_lowercase)
        generated_strings.append(current_string)
    return generated_strings

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