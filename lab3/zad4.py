

def init():
    a = int(input("podaj a"))
    r = int(input("podaj r"))
    n = 1
    while 1:
        n = int(input("podaj naturalną n"))
        if n >=0:
            break
    for i in range(1,n+1):
        print(a+ (i-1)*r)
init()