import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('flights.csv')
print(df)
fig, axes = plt.subplots(1, 3, figsize=(16, 8));
flights_by_cargo = df.groupby(['CARGO']).size().plot(kind='bar', title='Number of flights',ax=axes[0],sharex=True)
weight_by_cargo = df[['CARGO', 'WEIGHT']].groupby(['CARGO']).sum()
price_by_cargo = df[['CARGO', 'PRICE']].groupby(['CARGO']).sum()
ax2 = weight_by_cargo.plot(kind='bar', title='Total weight', legend=False, ax=axes[1], sharex=True)
ax3 = price_by_cargo.plot(kind='bar', title='Total price', legend=False, ax=axes[2], sharex=True)
plt.show()