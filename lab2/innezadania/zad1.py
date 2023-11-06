

def init():
    x = int(input("Podaj x"))
    y = int(input("Podaj y"))
    if x>y:
        x,y=y,x
    while x<=y:
        print(x)
        x+=1

init()