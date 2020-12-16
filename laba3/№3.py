import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 4, figsize=(16, 8));
student_data = pd.read_excel('students_info.xlsx')
results = pd.read_html('results_ejudge.html')[0] #[0]: list --> DataFrame

print(student_data)
print('=====================')
#print(results.dtypes)
df = results.merge(student_data, left_on = 'User', right_on = 'login')
print('=====================')
print(df)
print('=====================')

solved_by_group_faculty = df[['group_faculty', 'Solved']].groupby(['group_faculty']).mean()
solved_by_group_faculty.plot(kind='bar', title='Solved tasks by faculty', legend =   False, ax=axes[0], sharex=True)


solved_by_group_out = df[['group_out', 'Solved']].groupby(['group_out']).mean()
solved_by_group_out.plot(kind='bar', title='Solved tasks by group out', legend =   False, ax=axes[1], sharex=True)

top_users = df[(df.G>=10) | (df.H>=10)]
print(top_users)


top_users.groupby(['group_faculty']).size().plot(kind='bar', title='Group faculty for top users',ax=axes[2], sharex=True)


top_users.groupby(['group_out']).size().plot(kind='bar', title='Group out for top users',ax=axes[3], sharex=True)
plt.show()