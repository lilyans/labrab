import pandas as pd
import numpy as np

df = pd.read_csv('transactions.csv')
print(df)
print('=====================')
sorted_df = df[df.STATUS == 'OK'].sort_values('SUM', ascending=False)
print(sorted_df.head(3))
print('=====================')
total_sum = sum(df[(df.STATUS=='OK')&(df.CONTRACTOR=='Umbrella, Inc')]['SUM'])
print(total_sum)