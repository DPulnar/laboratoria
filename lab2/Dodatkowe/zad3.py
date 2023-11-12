
def Konwertujnabool(x):
    if x.lower() == "tak":
        return  1
    elif x.lower()=="nie":
        return  0

def init():
    czypada = input("czy pada")
    czypada = Konwertujnabool(czypada)
    czyautobus = input("czy jest autobus")
    czyautobus = Konwertujnabool(czyautobus)


    if czypada and czyautobus:
        print("Weż parasol \n","Dostaniesz się na uczelnie")
    elif czypada and not czyautobus:
        print("Nie dostaniesz się na uczelnie")
    elif not czypada and czyautobus:
        print("Dostaniesz się na uczelnie \n","Miłego dnia i pięknej pogody")

init()