




def init():
    liczba = int(input("Podaj liczbe"))

    silnia = liczba
    for i in range(liczba-1,0,-1):
        # print(i)
        silnia*=i
    print(silnia)
init()