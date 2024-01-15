import time

ile_sekund = int(input("podaj ile sekund do konca"))


for i in range(ile_sekund,-1,-1):
    print(i)
    time.sleep(1)