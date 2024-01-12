def potega(a, n):
   if n == 0:
       return 1
   else:
       return a * potega(a, n-1)

a = int(input("Podaj liczbę: "))
n = int(input("Podaj potęgę: "))
print("wynik: ", potega(a, n))