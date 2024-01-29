import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
df['ocena'].plot(kind='bar', title='Wykres ocen',position=1,width=0.3)
df_2['ocena'].plot(kind='bar', title='Wykres ocen 2',color='r',position=2,width=0.3)
pozycje_x=np.arange(4)
plt.legend(["termin 1",'termin 2'])
plt.xticks(pozycje_x, df['imie']+" "+df['nazwisko'])
plt.show()