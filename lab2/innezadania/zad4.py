def init():
    x = int(input("Podaj x"))
    y = int(input("Podaj y"))
    if x>y:
        x,y=y,x
    while x<=y:
        if x % 2 !=0:
            x += 1
            continue
        print(x)
        x+=1

init()