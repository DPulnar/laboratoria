
tekst = "python jest super"

print(tekst[0])
print(tekst[len(tekst)-1])
print("CO DRUGI")
for i in tekst[0:len(tekst):2]:
    print(i)
print("CO trzeci")
for i in tekst[0:len(tekst):3]:
    print(i)
print("OD DZIESIATEGO DO OSTATNIEGO")
for i in tekst[9::-1]:
    print(i)
# for i in range(10, -1, -1):
#     print(tekst[i],i)
print("OD KONCA DO POCZATKU")
# for i in range(len(tekst)-1, -1,-1):
#     print(tekst[i],i)
for i in tekst[::-1]:
    print(i)