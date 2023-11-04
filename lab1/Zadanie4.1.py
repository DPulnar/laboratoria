

import random



cenazalitr = 6.5
def init():
    avgspalanie = float(input("Podaj srednie spalanie"))
    droga   = random.randint(1,100000)
    zuzyciepaliwa = (avgspalanie/100)*droga
    kosztpaliwa = zuzyciepaliwa*cenazalitr
    print(f"zuzyciepaliwa: {round(zuzyciepaliwa,2)} l", f"koszt: {round(kosztpaliwa,2)}zł")


init()