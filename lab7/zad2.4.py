import matplotlib.pyplot as plt

oceny = [3, 4, 5, 3, 4, 5, 5, 4, 3, 4]

plt.hist(oceny, bins=[2, 3, 4, 5, 6], edgecolor='black')
plt.xlabel('Oceny')
plt.ylabel('Częstotliwosc')
plt.show()