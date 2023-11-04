


def PodajWartosci():
    droga = int(input("podaj pokonaną droge w km: "))
    avgspalanie = float(input("podaj srednie spalanie: "))
    return droga,avgspalanie



cenazalitr = 6.5
def init():
    droga,avgspalanie = PodajWartosci()
    zuzyciepaliwa = (avgspalanie/100)*droga
    kosztpaliwa = zuzyciepaliwa*cenazalitr
    print(f"zuzyciepaliwa: {round(zuzyciepaliwa,2)} l", f"koszt: {round(kosztpaliwa,2)}zł")


init()