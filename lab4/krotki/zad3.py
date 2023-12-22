rachunki = {
   "Styczeń": 100,
   "Luty": 120,
   "Marzec": 110,
   "Kwiecień": 130,
   "Maj": 115,
   "Czerwiec": 125,
   "Lipiec": 120,
   "Sierpień": 135,
   "Wrzesień": 120,
   "Październik": 115,
   "Listopad": 110,
   "Grudzień": 120
}
max_rachunek = max(rachunki.values())
min_rachunek = min(rachunki.values())
sum_rachunek = sum(rachunki.values())
avg_rachunek = sum_rachunek/ len(rachunki)
print(max_rachunek,min_rachunek,sum_rachunek,avg_rachunek)

ostatni_miesiac = "Grudzień"
if rachunki[ostatni_miesiac] > avg_rachunek:
   print("Zacznij oszczędzać")
else:
   print("Jesteś bezpieczny")