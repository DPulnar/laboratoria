import math


def PodajBoki():
    a = float(input("podaj bok a: "))
    b = float(input("podaj bok b: "))
    c = float(input("podaj bok b: "))
    return a,b,c


def init():
    a,b,c = PodajBoki()
    p = (a+b+c)/2
    pole = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"Pole: {pole}")

init()