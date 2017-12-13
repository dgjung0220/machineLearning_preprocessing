# Day_03_03_pandas_movie.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# UserID::MovieID::Rating::Timestamp
# UserID::Gender::Age::Occupation::Zip-code
# MovieID::Title::Genres

pd.set_option('display.width', 1000)

def get_data():
    users = pd.read_csv('ml-1m/users.dat',
                        sep='::',                                               # separator
                        engine='python',                                        #
                        names=['UserID','Gender','Age','Occupation','Zip-code'])# header
    movies = pd.read_csv('ml-1m/movies.dat',
                        sep='::',                                               # separator
                        engine='python',                                        #
                        names=['MovieID','Title','Genres'])                     # header

    ratings = pd.read_csv('ml-1m/ratings.dat',
                        sep='::',                                               # separator
                        engine='python',                                        #
                        names=['UserID','MovieID','Rating','Timestamp'])        # header

    data = pd.merge(pd.merge(ratings, users), movies)

    return data

def basic_pivot():
    data = get_data()
    t1 = data.pivot_table(values='Rating', columns='Gender')
    print(t1)

    t2 = data.pivot_table(values='Rating', columns='Gender', index='Age')
    print(t2)

    t2.index = ["Under 18","18-24","25-34","35-44","45-49","50-55","56+"]
    print(t2)

    # 문제
    # t2를 막대 그래프로 그려보세요.
    t2.plot(kind='bar')
    # plt.show()
    print('-' * 50)

    t3 = data.pivot_table(values='Rating', index=['Gender', 'Occupation'])
    t4 = data.pivot_table(values='Rating', index='Age', columns=['Gender', 'Occupation'],
                          fill_value=0)     # 없는 값은 0으로 채워줌.

    t6 = data.pivot_table(values='Rating', index=['Gender', 'Age'])
    print(t6)
    print(t6.unstack())                 # unstack() : 쌓지 않고 가로로 길게 그려 줌. # index->column
    print(t6.unstack().stack())         # column -> index 로.
    print('-' * 50)

    t7 = data.pivot_table(values='Rating', index='Age', columns='Gender', aggfunc='sum')    # aggfunc 집계 함수
    print(t7)
    print('-' * 50)

    # t8 = data.pivot_table(values='Rating', index='Age', columns='Gender', aggfunc=['mean','sum'])   # Error, 함수 연산 복수개는...
    # t8 = data.pivot_table(values='Rating', index='Age', columns='Gender', aggfunc=[np.mean,np.sum])

    t8_1 = data.pivot_table(values='Rating', index='Age', columns='Gender', aggfunc=[np.mean])
    print(t8_1)
    t8_2 = data.pivot_table(values='Rating', index='Age', columns='Gender', aggfunc=[np.sum])
    print(t8_2)

    print(pd.concat([t8_1, t8_2]))
    print(pd.concat([t8_1, t8_2], axis=1))

def get_index_500(data) :
    count_by_title = data.groupby('Title').size()
#    print(count_by_title)
#    print(count_by_title >= 500)        # boolean 배열 생성

    count_500 = count_by_title[count_by_title >= 500]
#    print(count_500)

    index_500  = count_by_title.index[count_by_title >= 500]        # 영화 데이터만 출력
#    print(index_500)
    return index_500


data = get_data()
index_500 = get_index_500(data)

by_gender = pd.DataFrame.pivot_table(data, values='Rating', index='Title', columns='Gender')
rating_500 = by_gender.loc[index_500]
print(rating_500)

# 문제
# 여성들이 가장 좋아하는 영화 top5를 찾아보세요.
top_female = rating_500.sort_values(by='F', ascending=False)
print(top_female[:5])

# 문제
# 여성들이 남성들보다 좋아하는 영화 Top5를 찾아 보세요.
rating_500['diff'] = rating_500['F'] - rating_500['M']
female_better = rating_500.sort_values(by='diff', ascending=False)
print(female_better.head())

# 여성과 남성 모두 편차 없는 영화를 찾아 보세요.
rating_500['Dist'] = (rating_500['F'] - rating_500['M']).abs()
top_movie = rating_500.sort_values(by='Dist')
print(top_movie.head())

rating_std = data.groupby('Title')['Rating'].std()          # 편차 standard
print(rating_std)

print(rating_std.loc[index_500])
