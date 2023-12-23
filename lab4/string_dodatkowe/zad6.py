zdanie = input("podaj zdanie")
if zdanie == zdanie[::-1]:
  print("Ciąg jest palindromem.")
else:
  print("Ciąg nie jest palindromem.")