def PodajLiczby():
    x = float(input("podaj liczbe x: "))
    y = float(input("podaj liczbe y: "))
    if y==0:
        while y==0:
            y = float(input("podaj liczbe y: "))
    return x,y


def oblicz(dzialanie,x,y)
    if dzialanie == "dodawianie":
        return  x+y
    elif dzialanie == "odejmowanie":
        return x-y
    elif dzialanie == "mnozenie":
        return x * y
    elif dzialanie == "dzielenie":
        return  x/y
def init():
    x,y = PodajLiczby()
    dzialanie = input("podaj działanie")
    wynik = oblicz(dzialanie,x,y)
    print(wynik)

init()