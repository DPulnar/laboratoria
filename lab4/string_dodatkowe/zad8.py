import string
alfabet = list(string.ascii_lowercase)

n = int(input("podaj n"))
nowa_lista = []

j= 0
for i, v in enumerate(alfabet):
    if (i+1)%3==0:
       nowa_lista.append([alfabet[i-2],alfabet[i-1],alfabet[i]])
       j+=1
    if i== len(alfabet)-1:
       nowa_lista.append([alfabet[i - 1], alfabet[i]])

print(nowa_lista)