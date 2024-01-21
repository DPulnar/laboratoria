import math
import random


szczesliwy_numerek = random.randint(0,16)

tablica = [2002,2003,2004,2005]
szczesliwy_rocznik = random.randint(0,len(tablica)-1)
print(tablica[szczesliwy_rocznik])


#C
lista = list(range(1,50))
sample =random.sample(lista,6)
print(sample)