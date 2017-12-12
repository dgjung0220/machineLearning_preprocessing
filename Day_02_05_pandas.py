# Day_02_05_pandas.py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def not_used1() :
    s = pd.Series([5,1,2,9])
    print(s)

    print(s.values)                                             # [5 1 2 9]
    print(s.index)                                              # RangeIndex(start=0, stop=4, step=1)
    print('-' * 50)

    s2 = pd.Series([5, 1, 2, 9], index = ['a', 'b', 'c', 'd'])
    print(s2)

    print(s2[0], s2[1], s2[2], s2[3])
    print(s2['a'], s2['b'])                                     # index 이름으로 접근 가능.
    print('-' * 50)

    s3 = pd.Series({'a' : 5, 'b':1,'c':2,'d':9})                # dictionary 를 이용해서도 만들 수 있다.
    print(s3)

# 컴프리헨션 Comprehension
def not_used2():
    print([i for i in range(5)])                                    # 0~4 까지의 리스트 만들기
    print([0 for i in range(5)])                                    # 0 0 0 0 0
    print(['test' for i in range(5)])                               # 'test' 'test' 'test' 'test' 'test'

def not_used3():
    np.random.seed(42)
    baby_names = ['Bob', 'Jessica', 'Mary', 'John', 'Melony']
    names = [baby_names[np.random.randint(len(baby_names))] for _ in range(1000)]
    births = [np.random.randint(1000) for _ in range(1000)]

    baby_sets = list(zip(names, births))

    # for item in baby_sets:
    #    print(item)

    df = pd.DataFrame(baby_sets, columns=['Name', 'Birth'])
    print(df)
    print(type(df.values))                  # numpy.ndarray
    print(df.index)
    print(df.columns)
    print('-'* 50)

    print(df.head(2))                       # 갯수 지정 가능
    print(df.tail(2))

    name_by = df.groupby('Name')
    print(name_by)
    print(name_by.sum())                    # 이름별로 sum()
    print(name_by.size())                   # 이름별로 size()-갯수
    print(name_by.size().sum())             # 1000

    # name_by.sum().plot()
    name_by.size().plot(kind='bar')
    plt.subplots_adjust(bottom=0.2, top=0.9)
    plt.show()

df = pd.DataFrame({'state' : ['San Francisco', 'San Francisco', 'San Francisco', 'LA', 'LA', 'LA'],
                   'year' : [2000 , 2001, 2002, 2000, 2001, 2002],
                   'population': [1.5, 1.7, 3.6, 2.4, 2.9 ,2.8]})
df.index = ['one', 'two', 'three', 'four', 'five', 'six']
# print(df)
#        population          state  year
# one           1.5  San Francisco  2000
# two           1.7  San Francisco  2001
# three         3.6  San Francisco  2002
# four          2.4             LA  2000
# five          2.9             LA  2001
# six           2.8             LA  2002

# print(df['population'])
# print(df['population']['three'])

print(df.population)        # print(df['population']) 과 출력상으론 동일. 안 되는 연산이 가끔 있다.
print('-' * 50)

print(df.iloc[2])           # ilocation, 행으로 탐색
print(df.loc['three'])      # location loc[' '] 행으로 탐색

print(df.ix[2])             # ix, 행으로 탐색
print(df.ix['three'])
print('-' * 50)

print(df.iloc[2][0])
print(df.iloc[2][1])

print(df.iloc[1:3])         #
print(df.loc['two':'four']) # 이 경우에 대해서만 마지막 데이터가 포함된다. (slicing)

