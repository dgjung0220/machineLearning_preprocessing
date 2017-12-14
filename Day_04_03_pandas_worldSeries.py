# Day_04_03_pandas_worldSeries.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.width = 1000
np.set_printoptions(linewidth=1000)

path = 'world-series/world-series/MLB World Series Champions_ 1903-2016.xlsx'
champs = pd.read_excel(path, index_col=0)

# 문제
# 구단 전체 개수
total_teams = champs.Champion
print(len(total_teams.unique()))

# 문제
# 100승 이상 팀만 알려주세요.
print(champs[champs.Wins>=100].Champion.unique())

# 문제
# 최다 우승 top5 팀을 알려주세요.
by_teams= champs.groupby('Champion').size()
print(by_teams)
by_sort = by_teams.sort_values(ascending=False)

team_top5 = by_sort[4]
print(team_top5)

top5 = by_sort[by_sort >= team_top5]
print(top5)

print('-' * 50)
# 문제
# 뉴욕 양키스의 최초 우승 년도와 마지막 우승 년도
ny_index = (champs.Champion == 'New York Yankees')
yankees = champs[ny_index]
print(yankees)
# 최초 우승
print(yankees.index[0])
# 마지막 우승
print(yankees.index[-1])
print('-' * 50)
# 문제
# 월드 시리즈가 개최되지 못 했던 연도?
# y1, y2 = champs.index[0], champs.index[-1]
y1, y2 = champs.index.min(), champs.index.max()
print(y1, y2)

# method1
years = pd.Index(range(y1, y2+1))
diff = years.difference(champs.index)
print(diff)

# method2
print([i for i in range(y1, y2+1) if not i in champs.index])

# method3
year_1 = np.arange(y1, y2+1)
year_2 = champs.index.values
print(np.setdiff1d(year_1, year_2))