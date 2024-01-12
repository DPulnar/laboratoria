def wspolne_elementy(lista1, lista2):
    wspolne = list()
    for element in lista1:
        if element in lista2:
            wspolne.append(element)
    return  wspolne
print(wspolne_elementy([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))