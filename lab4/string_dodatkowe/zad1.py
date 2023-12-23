
alfabet ="aąbcćdeęfghijkllłmnńoóprsśtuwyzźż"

zdanie = input("Wprowadź zdanie")
zdanie = zdanie.lower()

print(alfabet)
alfabet = list(alfabet)
używane_litery = list(zdanie)
for litera in używane_litery:
    if alfabet.index(litera)+1:
        alfabet.remove(litera)

print("nieużywane litery", alfabet)