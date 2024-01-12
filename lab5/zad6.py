import math

def pole_trójkąta(a, b, c):
   s = (a + b + c) / 2
   pole = math.sqrt(s*(s-a)*(s-b)*(s-c))
   return pole

while 1:
    a = float(input("Podaj długość boku a: "))
    b = float(input("Podaj długość boku b: "))
    c = float(input("Podaj długość boku c: "))
    if a >0 and b>0 and c>0 and max(a,b,c)<(a+b+c-max(a,b,c)):
        break
    else:
        print("podano złe wartości")

area = pole_trójkąta(a, b, c)
print("Pole trójkąta wynosi: ", area)
