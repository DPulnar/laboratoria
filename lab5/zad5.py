def bmi(wzrost, waga):
   return round((wzrost / waga**2), 2)

h = float(input("Podaj swój wzrost w metrach: "))
w = float(input("Podaj swoją wagę w kg: "))

bmi = bmi(h, w)
print("Twój wskaźnik BMI wynosi: ", bmi)

if bmi <= 18.5:
   print("Jesteś niedożywiony.")
elif 18.5 < bmi <= 24.9:
   print("Twoja waga jest prawidłowa.")
elif 25 < bmi <= 29.29:
   print("Jesteś przekroczony.")
else:
   print("Jesteś przebudzony.")
