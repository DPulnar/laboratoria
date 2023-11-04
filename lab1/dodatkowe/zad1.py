
def PodajArgumenty():
    a = float(input("podaj wspolczynnik a: "))
    b = float(input("podaj wspolczynnik b: "))
    return a,b


def init():
    a,b = PodajArgumenty()
    rozwiazanie = -b/a
    print(f"rozwiazanie {rozwiazanie}")

init()