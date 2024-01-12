def wypisz(imie,wiek=20):
    """wypisuje imie i wiek"""
    print(imie,wiek)

imie = input("podaj imie")
wiek = input("podaj wiek")
wypisz(imie,wiek)
print(wypisz.__doc__)