

def init():
    wysokosc = int(input("podaj wysokosc choinki"))
    for dlugoscwiersza in range(1,wysokosc+1):
        tekst = " * "
        spacje = " "
        for d in range(dlugoscwiersza,wysokosc+1):
            spacje+=" "
        for j in range(0,dlugoscwiersza-1):
            tekst+=" * "
        print(spacje+tekst)


init()
