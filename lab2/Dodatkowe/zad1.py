

#zapewne chodzilo w zadaniu aby zrobic to bez wbudowanych funkcji

duze = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ"
male = "aąbcćdeęfghijkllłmnńoóprsśtuwyzźż"

x = input("podaj  litere")
for litera in duze:
    if litera == x:
        print("Jest dużą literą")
        break
for litera in male:
    if litera == x:
        print("Jest małą literą")
        break