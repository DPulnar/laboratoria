def init():
    n = int(input("podaj liczbe studentow"))

    i = 1
    suma = 0
    while 1:
        x = int(input(f"podaj liczbe punktow dla {i} studenta"))
        if x<0 and x >100:
            continue
        suma+=x
        i+=1
        if i==n+1:
            break
    print(f"srednia punktow wynosci {suma/n}")
init()