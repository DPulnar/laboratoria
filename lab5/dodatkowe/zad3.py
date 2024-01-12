import math

def oblicz_pierwiastki(a, b=0, c=0):
 delta = b**2 - 4*a*c
 if delta < 0:
    return 0
 else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return (x1, x2)

print(oblicz_pierwiastki(1, -3, 2))
