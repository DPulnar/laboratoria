def czy_anagram(slowo1,slowo2):
    litery = dict()

    for litera in slowo1:
        if not litera in litery:
            if  litery.get(litera)==None:
                litery[litera]=1

            litery[litera]+=1
    slowo2lista = list(slowo2)
    for litera in litery:
        if not slowo2lista.count(litera) == litery[litera]:
            print("nie jest anagramem")
            return 0
    print("jest anagramem")
    return 1

czy_anagram("aabb","abba")