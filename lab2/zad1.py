



def init():
    age = int(input("Podaj wiek"))
    cena = 20
    if age < 18 and age>4:
        cena = 10
    else:
        cena = 0
    print(f"Cena wynosi: {cena}")