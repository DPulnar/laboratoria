


def init():
    a = int(input("Podaj a"))
    b =  int(input("Podaj b"))
    c =  int(input("Podaj c"))
if a!= 0:
    delta = b ** 2 - 4 * a * c
    pierwdelta = delta ** (1 / 2)
    if delta == 0:
        wynik = (-b) / (2 * a)
        print(wynik)
    elif delta > 0:
        wynik1 = (-b - pierwdelta) / (2 * a)
        wynik2 = (-b + pierwdelta) / (2 * a)
        print(wynik1, wynik2)
    else:
        print("Nie ma rozwiazan")
else:
    print((-b)/a)



init()