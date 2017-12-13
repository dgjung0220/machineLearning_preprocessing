# Day_03_06_pandas_baby.py

import pandas as pd
import matplotlib.pyplot as plt

names = pd.read_csv('Data/yob1880.txt', names=['Name', 'Gender', 'Births'])


# 문제
# 1. 남자와 여자 이름의 갯수를 알려 주세요.
men = names[names['Gender'] == 'M']
# print(men)
print(len(men))                 # men.count()
women = names[names['Gender'] == 'F']
print(len(women))

by_gender = names.groupby(by='Gender').size()
print(by_gender)

# 2. 남자와 여자 이름의 갯수 합계를 알려 주세요.
print(men.Births.sum())
print(women.Births.sum())

print(by_gender.sum())

# 3. 남자 또는 여자 이름 top5 막대 그래프 그려주세요.
# men.head().plot(kind='bar')
# men.index = men.head().Name
# women.head().plot(kind='bar')

men_only = names[names.Gender == 'M']
men_sorted = men_only.sort_values('Births', ascending=False)
top5  = men_sorted[:5]

top5.index = top5.Name
del top5['Name']
top5.plot(kind='bar')
# plt.show()
print('-' * 50)

# 문제
# 남자와 여자 이름이 같은 데이터를 찾아보세요.
men_only = names[names.Gender == 'M']
women_only = names[names.Gender == 'F']

temp = pd.concat([men_only, women_only])
if_same = temp.groupby(by='Name').size()
print(if_same[if_same > 1].count())

# 선생님 풀이
by_names = names.pivot_table(values='Births', index='Name', columns='Gender')
by_size = names.groupby('Name').size()
print(by_size[by_size > 1].count())



