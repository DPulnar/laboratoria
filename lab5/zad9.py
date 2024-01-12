def fibonacci(n):
   if n <= 0:
       return "Wprowadź liczbę większą od 0."
   elif n == 1:
       return 0
   elif n == 2:
       return 1
   else:
       return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Podaj numer wyrazu ciągu Fibonacciego: "))
print("Wyraz ciągu Fibonacciego wynosi: ", fibonacci(n))