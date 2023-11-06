def PodajLiczby():
    x = float(input("podaj liczbe x: "))
    y = float(input("podaj liczbe y: "))
    if y==0:
        while y==0:
            y = float(input("podaj liczbe y: "))
    return x,y


def oblicz(dzialanie,x,y):
    if dzialanie == "1":
        return  x+y
    elif dzialanie == "2":
        return x-y
    elif dzialanie == "3":
        return x * y
    elif dzialanie == "4":
        return  x/y
    elif dzialanie == "6":
        return  x**y
def init():
    x,y = PodajLiczby()
    dzialanie = input("podaj działanie")
    wynik = oblicz(dzialanie,x,y)
    print(wynik)

init()