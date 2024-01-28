import pandas as pd
import matplotlib.pyplot as plt

data = {
    'nr_albumu':[69998,69997,69996,69995],
    'imie': ["Janusz","Tomasz","Dominik","Wiktor"],
    "nazwisko":["Nowak","Murjas","Pulnar","Bałon"],
    "wiek": [21,37,20,20],
    "ocena":[4,4,5,2]
}
df = pd.DataFrame(data)
data2 = {
    'nr_albumu':[69998,69997,69996,69995],
    'imie': ["Janusz","Tomasz","Dominik","Wiktor"],
    "nazwisko":["Nowak","Murjas","Pulnar","Bałon"],
    "wiek": [21,37,20,20],
    "ocena":[4,4,5,4]
}
df_2 = pd.DataFrame(data2)
#a
