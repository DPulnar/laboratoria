import pandas as pd
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo

automobile = fetch_ucirepo(id=10)

X = automobile.data.features
df = pd.DataFrame(X)

df.plot(kind='scatter', x='horsepower', y='price')
plt.show()
