
tekst = "python jest super"

print(tekst[0])
print(tekst[len(tekst)-1])
print("CO DRUGI")
for i in range(0,len(tekst),2):
    print(tekst[i])
print("CO trzeci")
for i in range(0, len(tekst), 3):
    print(tekst[i])
print("OD DZIESIATEGO DO OSTATNIEGO")
for i in range(10, -1, -1):
    print(tekst[i],i)
print("OD KONCA DO POCZATKU")
for i in range(len(tekst)-1, -1,-1):
    print(tekst[i],i)