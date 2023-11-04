def PodajLiczby():
    x = float(input("podaj liczbe x: "))
    y = float(input("podaj liczbe y: "))
    if y==0:
        while y==0:
            y = float(input("podaj liczbe y: "))
    return x,y


def init():
    x,y = PodajLiczby()
    print(f"dodawanie: {x + y}")
    print(f"odejmowanie: {x - y}")
    print(f"mnozenie: {x * y}")
    print(f"dzielenie: {x / y}")


init()