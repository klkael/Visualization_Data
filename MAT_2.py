import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im

df = pd.read_csv('DataSales.csv')
df = df.pivot(index='nama',columns='mobil')
print(df)
plt.imshow(df)
plt.colorbar()
plt.show()