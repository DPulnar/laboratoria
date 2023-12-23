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
lista = generuj(n,x)
print(lista)
#a
suma = 0
for v in lista:
    suma+=len(v)
print(suma)
#b
ilosc_k =0
for v in lista:
   ilosc_k+=v.count('k')
print(ilosc_k,"ilosc liter k")
#c
ilosc_k =0
for v in lista:
   ilosc_k+=v.count('kt')
print(ilosc_k,"ilosc kt")
#d
dlugosc = 0
s = int(input("podaj s"))
for v in lista:
    if len(v)> s:
        dlugosc += 1
print("ile ciagow znakow dluzszych niz S:",dlugosc)
#e
for i,v in enumerate(lista):
    lista[i]= "a"+lista[i]+"z"
print(lista)