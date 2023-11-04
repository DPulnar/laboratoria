
def PodajBoki():
    x = int(input("podaj pierwszy bok: "))
    y = int(input("podaj drugi bok: "))
    return x,y


def init():
    x,y = PodajBoki()
    pole = x*y
    obwod = 2*x+2*y
    print(f"pole:{pole} ",f"Obwod: {obwod}")

init()