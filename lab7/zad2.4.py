import matplotlib.pyplot as plt
import pandas as pd

data = {
    'nr_albumu':[69998,69997,69996,69995],
    'imie': ["Janusz","Tomasz","Dominik","Wiktor"],
    "nazwisko":["Nowak","Murjas","Pulnar","Bałon"],
    "wiek": [21,37,20,20],
    "ocena":[4,4,5,2]
}
df = pd.DataFrame(data)
df['ocena'].hist(bins=5, edgecolor='black')
plt.title('Rozkład ocen')
plt.xlabel('Ocena')
plt.ylabel('Ilość')
plt.show()