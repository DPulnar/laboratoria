class kalkulator:

    def __init__(self, x, y,dzialanie):
        self.x = x
        self.y = y
        self.dzialanie = dzialanie
    def oblicz(self):
        if self.dzialanie == "dodawianie":
            return x + y
        elif self.dzialanie == "odejmowanie":
            return x - y
        elif self.dzialanie == "mnozenie":
            return x * y
        elif self.dzialanie == "dzielenie":
            return x / y
def PodajLiczby():
    x = float(input("podaj liczbe x: "))
    y = float(input("podaj liczbe y: "))
    if y==0:
        while y==0:
            y = float(input("podaj liczbe y: "))
    return x,y
def init():
    x,y = PodajLiczby()
    dzialanie = input("podaj działanie")
    calc = kalkulator(x,y,dzialanie)
    wynik = calc.oblicz()

init()
# def oblicz(dzialanie,x,y)
#     if dzialanie == "dodawianie":
#         return  x+y
#     elif dzialanie == "odejmowanie":
#         return x-y
#     elif dzialanie == "mnozenie":
#         return x * y
#     elif dzialanie == "dzielenie":
#         return  x/y


