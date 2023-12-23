
rozmiar_pola = (6, 5)


pozycje_przeciwnikow = [(0, 1), (2, 3), (2, 4), (3, 4)]


pozycje_monet = [(1, 1), (2, 0), (3, 3), (5, 3)]



pole_gry = []
for x in range(rozmiar_pola[0]):
  pole_gry.append([])
  for y in range(rozmiar_pola[1]):
    pole_gry[x].append('.')
print(pole_gry)

for przeciwnik in pozycje_przeciwnikow:
  pole_gry[przeciwnik[0]][przeciwnik[1]] = 'x'


for moneta in pozycje_monet:
  pole_gry[moneta[0]][moneta[1]] = '*'

for i in range(rozmiar_pola[0]):
  pole_gry[i][2]= "="


for wiersz in pole_gry:
  print(' '.join(wiersz))