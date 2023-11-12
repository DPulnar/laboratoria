def init():
    n = int(input("podaj liczbe studentow"))

    i = 1
    suma = 0
    while i<=n:
        x = int(input(f"podaj liczbe punktow dla {i} studenta"))
        if x<0 or x >100:
            continue
        suma+=x
        i+=1
    print(f"srednia punktow wynosci {suma/n}")
init()