

def init():
    x = int(input("podaj wysokosc choinki"))
    for i in range(1,x+1):
        tekst = " * "
        for j in range(0,i-1):
            tekst+=" * "
        print(tekst)


init()
