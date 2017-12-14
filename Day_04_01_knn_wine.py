# Day_04_01_knn_wine.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection, neighbors, linear_model, preprocessing

pd.set_option('display.width', 1000)            # pandas print option
np.set_printoptions(linewidth=1000)             # numpy print option

df = pd.read_csv('Data/winequality-red.csv', sep=';')
# print(df)

# histogram 데이터 분포 살펴보기
# pd.DataFrame.hist(df, figsize=[20, 9])             # figsize 단위 inch-
# plt.show()

all_quality = df.quality.values
print(all_quality)
print(df['quality'].unique())                       # Unique 한 값

# 문제
# 좋은/나쁜 포도주의 합계를 구하시오
# bad - 3,4,5 Good - 6,7,8
good_wine = df[df['quality'].values > 5]
bad_wine = df[df['quality'].values <= 5]

print(len(good_wine))
print(len(bad_wine))
print(len(good_wine) + len(bad_wine))

# plt.subplot(1, 2, 1)
# plt.hist(all_quality)
# plt.subplot(1, 2, 2)
# plt.hist(df['quality'].values <= 5)
# plt.show()

# 센서의 답
by_quality = df.groupby('quality').size()
print(by_quality)
# good_win
print(by_quality.iloc[:3].sum())
# bad_wine
print(by_quality.iloc[3:].sum())

# good_win
print(by_quality.loc[:5].sum())
# bad_wine
print(by_quality.loc[6:].sum())

x = df.drop(labels='quality', axis=1)           # drop label 하나를 가리킨다. (행/열), axis=1 column
y = (df.quality.values > 5)
print(x.shape, y.shape)

# 75:25 로 분할
data = model_selection.train_test_split(x, y, random_state=42)
train_x, test_x, train_y, test_y = data

knn = neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit(train_x, train_y)
print('score : ', knn.score(test_x, test_y))

y_hat = knn.predict(test_x)
print(y_hat)
print(test_y)
print('-' * 50)
# --------------------------------------------------------------------------------------- #
# 성능을 높이기 위해..
# scaling # z-score
scaler = preprocessing.StandardScaler()
x = scaler.fit_transform(x)

data = model_selection.train_test_split(x, y, random_state=42)
train_x, test_x, train_y, test_y = data

knn = neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(train_x, train_y)
print('score : ', knn.score(test_x, test_y))