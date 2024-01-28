import matplotlib.pyplot as plt

kategorie = ['A', 'B', 'C', 'D']
sprzedane_produkty = [10, 20, 15, 25]
plt.pie(sprzedane_produkty, labels=kategorie,
autopct='%1.f%%', startangle=90,
colors=['skyblue', 'lightgreen',
'lightcoral', 'gold'])
plt.title('Udział w kategoriach')
plt.show()