

zdanie = input("podaj zdanie")
wynik = ""
for wyraz in zdanie.split():
    wyrazlista = list(wyraz)
    wyrazlista[0] = wyrazlista[0].capitalize()
    wyrazlista[len(wyrazlista)-1] = wyrazlista[len(wyrazlista)-1].capitalize()
    wyrazlista = ''.join(wyrazlista)
    wynik+= wyrazlista
    wynik+=" "
print(wynik)

