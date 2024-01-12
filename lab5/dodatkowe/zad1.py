def okresl_plec(imię):
 if imię[-1] =='a':
    return "kobieta"
 else:
    return "mężczyzna"

imiona = ["Anna", "Tomasz", "Zofia", "Piotr", "Maria"]
slownik = dict()
for imie in imiona:
    plec = okresl_plec(imie)
    slownik[imie]= plec
print(slownik)
