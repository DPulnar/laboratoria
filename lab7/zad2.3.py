import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.xlabel('Czas')
plt.ylabel('Prędkosc chwilowa')
plt.scatter(x, y)
plt.show()