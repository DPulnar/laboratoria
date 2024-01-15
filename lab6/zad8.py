import math

a = int(input("podaj dlugosc boku a"))
b = int(input("podaj dlugosc boku b"))
kat = int(input("podaj kat pomiedzy bokami"))

if a >0 and b>0 and kat<180:
    if kat < 90:
        print("ostrokatny")
    pole = 0.5*a*b*math.sin(math.radians(kat))
    print(pole)
else:
    print("trojkat nie istnieje")
