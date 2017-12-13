# Day_03_02_pandas.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data/scores.csv')
# print(df)

# 문제
# ben 데이터를 출력하는 3가지 방법
print(df.iloc[2])
print(df.loc[2])
print(df.ix[2])
print('-' * 50)

# 열 탐색
print(df['kor'])
print(df.kor)
print('-' * 50)

# 여러 열 탐색
subjects = ['kor', 'mat', 'eng', 'bio']
print(df[subjects])
print(df[subjects[::-1]])                   # reverse
print('-' * 50)

print(type(df[subjects]))                   # <class 'pandas.core.frame.DataFrame'>
print(df[subjects].sum())
print(df[subjects].sum(axis=0))             # 열 단위로 sum()
print(df[subjects].sum(axis=1))             # 행 단위로 sum()

print(type(df[subjects].sum(axis=1)))       # <class 'pandas.core.series.Series'>
print(df[subjects].sum(axis=1).sum())       # Series Sum()
print('-' * 50)

# 문제
# 과목 평균을 구해보세요.
n = len(df)
print(df[subjects].mean())
# print(df[subjects].sum(axis=0) / n)
# print(df[subjects].mean(axis=0))
# 각 학생의 평균을 구해 보세요.
# print(df[subjects].sum(axis=1) / len(subjects))
print(df[subjects].mean(axis=1))
print('-' * 50)

# column 추가
df['sum'] = df[subjects].sum(axis=1)
df['avg'] = df[subjects].mean(axis=1)
print(df)
print('-' * 50)

print(df.sort_values('avg'))                    # 오름 차순 정렬
print(df.sort_values('avg', ascending=False))   # 내림 차순 정렬
print('-' * 50)

sorted_df = df.sort_values('avg', ascending=False)
sorted_df.index = sorted_df['name']             # index 를 이름으로 정렬
del sorted_df['name']                           # column 'name' 삭제
print(sorted_df)
print(sorted_df.index)                          # Index 배열 반환
print(sorted_df.index.values)                   # 값 배열 반환

# sorted_df['avg'].plot(kind='bar')
# plt.show()

# 문제
# 1반 학생만 출력
class_1st = df.sort_values('class')[df['class'] == 1]
print(class_1st)
print('-' * 50)

c1 = df[df['class'] == 1]
c2 = df[df['class'] == 2]

# c1.plot(kind='bar')
# plt.show()

plt.figure(1)
c1[subjects].boxplot()

plt.figure(2)
c2[subjects].boxplot()
plt.show()