

def init():

 przyklad = input("podaj ktory przyklad")
 if przyklad=="1":
  x = input("podaj imie")
  print("Witaj " + x)
 elif przyklad=="2":
  x = input("podaj wiek")
  print("Twój wiek to " + x)
 elif przyklad == "3":
  x = input("Podaj imie")
  y = input("Podaj nazwisko")
  print(x[0] + y[0])
 elif przyklad == "4":
  x = input("Podaj lancuch")
  for i in range(0, 5):
   print(x)
 elif przyklad == "5":
  x = input("Podaj lancuch")
  y = input("Podaj drugi lancuch")
  z = x + y
 elif przyklad == "6":
  x = input("Podaj lancuch")
  y = input("Podaj drugi lancuch")
  z = x[:(len(x) // 2)] + y[(len(x) // 2):]
  print(z)













init()