duze = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ"
male = "aąbcćdeęfghijkllłmnńoóprsśtuwyzźż"

def zamien_litere(x):
    for i, litera in enumerate(duze):
        if litera == x:
            # print("Jest dużą literą")
            return male[i]
    for i, litera in enumerate(male):
        if litera == x:
            # print("Jest małą literą")
            return duze[i]

x = input("podaj  litere")
x = zamien_litere(x)
print("zamieniona litera",x)