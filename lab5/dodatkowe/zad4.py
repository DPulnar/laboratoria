def zlicz_znaki(s):
    male =0
    duze =0
    inne = 0
    for znak in s:
        if znak.islower():
            male+=1
        elif znak.isupper():
            duze+=1
        else:
            inne+=1
    slownik = {
        "male":male,
        "duze": duze,
        "inne": inne

    }
    return  slownik


print(zlicz_znaki("TESTdsa"))