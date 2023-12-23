import random

cyfry = input("podaj 5 cyfr oddzielonych przecinkiem")

cyfry = cyfry.split(',')
if len(cyfry)==5:
    for i,v in enumerate(cyfry):
        cyfry[i]= int(cyfry[i])
    cyfry = set(cyfry)
    wybrana_cyfra = random.choice(list(cyfry))

    if wybrana_cyfra == min(cyfry) or wybrana_cyfra == max(cyfry):
        print("Wylosowałeś najmniejszą lub największą liczbę")
    else:
        print("Wylosowałeś liczbę, która nie jest ani najmniejszą, ani największą")