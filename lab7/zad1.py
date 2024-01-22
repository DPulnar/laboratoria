import pandas as pd

data = {
    'nr_albumu':[69998,69997,69996,69995],
    'imie': ["Janusz","Tomasz","Dominik","Wiktor"],
    "nazwisko":["Nowak","Murjas","Pulnar","Bałon"],
    "wiek": [21,37,20,20],
    "ocena":[4,4,5,2]
}
df = pd.DataFrame(data)
#a
print(df.query("ocena > 4"))
print("\n")
#b
print(df.sort_values("wiek"))
print("\n")
#c
print(df.groupby('ocena').get_group(4))
print("\n")
print(df.groupby('ocena')['wiek'].mean)
#d