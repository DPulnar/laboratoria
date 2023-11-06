





def init():
    x= int(input("Podaj x"))
    y = int(input("Podaj y"))
    z = int(input("Podaj z"))
    tosort= {x,y,z}
    tosort = list(tosort)
    for i in range(len(tosort)-1):
        if tosort[i]>tosort[i+1]:
            tosort[i],tosort[i + 1] = tosort[i+1],tosort[i]
    print(tosort)


init()