import random
a = int(input("podaj poczatek zakresu"))
b = int(input("podaj koniec zakresu"))
liczba_do_zgadniecia = random.randint(a,b)

zgadniete = 0
for i in range(3):
    zgadnij = int(input("zgadnij liczbe"))
    if zgadnij==liczba_do_zgadniecia:
        zgadniete = 1
        print("udalo ci sie zgadnac liczbe")
        break
    if zgadnij>liczba_do_zgadniecia:
        print("za duzo")
    else:
        print("za malo")
if not zgadniete:
    print("nie udalo ci sie zgadnac liczby")