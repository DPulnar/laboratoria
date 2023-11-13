

def init():

    while 1:
        x =int(input("Podaj liczbe nieujemna"))
        if x >=0:
            print("pierw",x**(1/2))
            continue
        print("dziekujemy za skorzystanie z naszej aplikacji")
        break

init()