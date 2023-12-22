import random


def stworz_zbior(ilosc_elementow):
    zbior = set()
    for i in range(ilosc_elementow):
        zbior.add(random.randint(0,10))
    return zbior

a = random.randint(3, 7)
b = random.randint(3, 7)

X = stworz_zbior(a)
Y = stworz_zbior(b)
print(X,Y)
#a
if 5 in X:
  print("Zbiór X zawiera liczbę 5.")
else:
  print("Zbiór X nie zawiera liczby 5.")
#b
if X.issubset(Y):
  print("Zbiór X jest podzbiorem zbioru Y")
else:
  print("Zbiór X nie jest podzbiorem zbioru Y")
#c
if Y.issubset(X):
  print("Zbiór Y jest podzbiorem zbioru X")
else:
  print("Zbiór Y nie jest podzbiorem zbioru X")
#d
if X.issuperset(Y):
  print("Zbiór X jest nadzbiorem zbioru Y")
else:
  print("Zbiór X nie jest nadzbiorem zbioru Y")
#e
if Y.issuperset(X):
  print("Zbiór Y jest nadzbiorem zbioru X")
else:
  print("Zbiór Y nie jest nadzbiorem zbioru X")
#f
print(X.union(Y),"Suma")

#g
print(X.difference(Y),"Różnica X i Y")
#h
print(Y.difference(X),"Różnica Y i X")
#i
print(X.intersection(Y),"iloczyn")
#j
print(X.symmetric_difference(Y),"różnica symetryczna")
#k
maks=0
if max(list(X))>max(list(Y)):
    maks =max(list(X))
else:
   maks =  max(list(Y))
print(maks,"maks")
#l
pierwszy_element= list(X)[0]
X.remove(pierwszy_element)
Y.add(pierwszy_element)
#m
kopia = X.copy()
for v in kopia:
    Y.add(v)
print(Y,"kopia")
#n
X.clear()
Y.clear()
print(X,Y)