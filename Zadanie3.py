
def PodajWartosci():
    x = int(input("podaj liczbę: "))
    y = int(input("podaj liczbę: "))
    return x,y


def init():
    x,y = PodajWartosci()
    pole = x*y
    obwod = 2*x+2*y
    print(f"pole:{pole} ",f"Obwod: {obwod}")

init()