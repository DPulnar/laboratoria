

def a():
    imie = input("podaj imie")
    print("witaj "+imie)
def b():
    wiek = input("podaj wiek")
    print("Twój wiek to: "+wiek)
def c():
    imie = input("podaj imie")
    nazwisko = input("podaj nazwisko")
    print(imie[0]+nazwisko[0])
def d():
    lancuch = input("podaj lancuch znakow")
    for i in range(1,5):
        print(lancuch)
def e():
    lancuch1 = input("podaj pierwszy lancuch znakow")
    lancuch2 = input("podaj drugi lancuch znakow")
    lancuch_finalny = lancuch1+lancuch2
def f():
    lancuch1 = input("podaj pierwszy lancuch znakow")
    lancuch2 = input("podaj drugi lancuch znakow")
    lancuch_finalny = lancuch1[0:(len(lancuch1)//2)] + lancuch2[(len(lancuch2)//2):]
    print(lancuch_finalny)
funkcje = {
    "a": a,
    "b": b,
    "c": c,
    "d": d,
    "e": e,
    "f": f,

}

def init():
    podpunkt = input("podaj ktory podpunkt")
    funkcje[podpunkt]()

init()