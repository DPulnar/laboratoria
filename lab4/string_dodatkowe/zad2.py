
zdanie = input("podaj zdanie")

wynik = ""
for i, v in enumerate(zdanie):
    if i%2==0:
        wynik += v

zdanie = wynik
print(zdanie)