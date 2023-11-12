

def ax(x):
    if x>0:
        return  2*x
    elif x<0:
        return -3*x
    return 0
def bx(x):
    if x>=1:
        return  x*x
    elif x<1:
        return x

def cx(x):
    if x>2:
        return  2+x
    elif x<2:
        return x-4
    return 2


#a(x)

def init():
    x = float(input("podaj argument funkcji a(x)"))
    wynik = ax(x)
    print("wynik",wynik)
###############################################
    x = float(input("podaj argument funkcji b(x)"))
    wynik = bx(x)
    print("wynik", wynik)
###############################################
    x = float(input("podaj argument funkcji c(x)"))
    wynik = cx(x)
    print("wynik",wynik)

init()