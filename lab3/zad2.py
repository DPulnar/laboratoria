

def init():
    x = int(input("podaj ilosc wierszy"))
    for i in range(1,x+1):
        for j in range(1,x+1):
            print(" * ", end="")
            if j == x:
                print("\n")

init()
