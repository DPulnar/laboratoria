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
print("a")
print(df.query("ocena > 4"))
print("\n")
#b
print("b")
print(df.sort_values("wiek"))
print("\n")
#c
print("c")
print(df.groupby('ocena').get_group(4))
print("\n")
print(df.groupby('ocena')['wiek'].mean())
#d
data2 = {
    'nr_albumu':[69998,69997,69996,69995],
    'imie': ["Janusz","Tomasz","Dominik","Wiktor"],
    "nazwisko":["Nowak","Murjas","Pulnar","Bałon"],
    "wiek": [21,37,20,20],
    "ocena":[4,4,5,4]
}
print("d")
df_2 = pd.DataFrame(data2)
polaczone = df.merge(df_2,how='right', on=['nr_albumu','imie','nazwisko','wiek','ocena'],copy=bool(0))
# polaczone =  pd.concat([df, df_2],axis=1, ignore_index=True, sort=False)

print(polaczone)
#e
polaczone.to_csv("studenci.csv",index=False)
#f
df_wczyt = pd.read_csv('studenci.csv')
#g
nowy = {'nr_albumu': 69992, 'imie': 'Arkadiusz', 'nazwisko': 'Rymarz',  'wiek': 20,'ocena': 5}
df_wczyt.loc[len(df_wczyt)]=nowy
print(df_wczyt)
#h
print(df_wczyt['ocena'].unique())
#i
print(len(df_wczyt.query("ocena == 5")))
