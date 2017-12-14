# Day_04_02_preprocessing.py
from sklearn.preprocessing import (add_dummy_feature, Binarizer, Imputer, LabelBinarizer, LabelEncoder, MaxAbsScaler, MinMaxScaler)

from sklearn import preprocessing
import numpy as np

def use_add_dummy_feature():
    x = [[1, 0], [0, 1]]
    print(x)
    print(add_dummy_feature(x))

    x = [[3, 1, 0], [9, 0, 1]]
    x = add_dummy_feature(x)
    x = add_dummy_feature(x)
    x = add_dummy_feature(x)
    print(x)

    x = add_dummy_feature(x, value=7)
    print(x)

    bias = np.ones([x.shape[0], 1])
    print(bias)
    x = np.hstack([bias, x])
    print(x)

def use_Binarizer():
    x = [[1.,-1,2.],
         [2.,0.,0.],
         [0.,1.,-1.]]
    scaler = Binarizer()
    scaler.fit(x)               # 필요없음.
    print(scaler.transform(x))

    scaler = Binarizer(threshold=1.5)
    print(scaler.transform(x))

    # Binarizer 단순 버전
    print(preprocessing.binarize(x))

def use_imputer():
    x = [[1,2],
         [np.nan, 3],
         [7,10]]

    # default 4 = (1+7) / 2
    # 5 = (2 + 3 + 10) / 3
    scaler = Imputer()
    scaler.fit(x)
    print(scaler.transform(x))

    # strategy : mean, median, most_frequent
    # scaler = Imputer(strategy='mean', axis=1)
    # scaler.fit(x)
    # print(scaler.transform(x))

    x1 = [[np.nan, 2],
         [6, np.nan],
         [7, 6]]
    print(scaler.transform(x1))

    print(scaler.statistics_)
    print(scaler.missing_values)

def use_localBinarizer():
    x = [1, 2, 6, 4, 2]
    lb1 = LabelBinarizer()
    lb1.fit(x)

    print(lb1.classes_)
    print(lb1.transform(x))

    # sparse array - 희소 행렬, 사이킷 런에서는 매개변수로 그냥 받는 경우가 많다.
    lb2 = LabelBinarizer(sparse_output=True)
    print(lb2.fit_transform(x))

    lb3 = LabelBinarizer(neg_label=-1, pos_label=1)
    print(lb3.fit_transform(x))
    print('-' * 50)

    # 범주형 데이터도 binary로 변환해준다.
    x2 = ['yes', 'no', 'no', 'yes']
    lb4 = LabelBinarizer()
    lb4.fit(x2)
    print(lb4.transform(x2))

    x3 = ['yes', 'no', 'no', 'yes', 'cancel']
    lb5 = LabelBinarizer()
    lb5.fit(x3)
    print(lb5.classes_)
    print(lb5.transform(x3))

    ix = lb5.transform(x3)
    print(lb5.inverse_transform(ix))
    print('-' * 50)
    # 문제
    # numpy를 사용하여 ix를 원본 데이터로 변환해 보세요.
    x_arg = np.argmax(ix, axis=1)
    print(x_arg)
    print(lb5.classes_[x_arg])

def use_LabelEncoder():
    x = [2, 3, 2, 6]
    le1 = LabelEncoder()
    le1.fit(x)

    print(le1.classes_)
    print(le1.transform(x))

    ix = le1.transform(x)
    print(le1.inverse_transform(ix))
    print('-'*50)

    x = ['tokyo', 'paris', 'tokyo', 'Germany']
    le2 = LabelEncoder()
    le2.fit(x)
    print(le2.classes_)
    print(le2.transform(x))

    print(le2.inverse_transform([0,0,2,2]))     # 새로운 결과 도출

def use_MaxAbsScaler():
    # 가장 큰 절대값 사용 : -1 ~ 1 사이로 변환
    x = [[1., -1., 5.],
         [2., 0., -5.],
         [0., 1., -10]]

    scaler = MaxAbsScaler()
    scaler.fit(x)
    print(scaler.transform(x))

def use_MinMaxScaler():
    # 열 기준, min, max 로 -1 ~ 1
    x =[[1. , -1., 2.],
        [2., 0., 0.],
        [0., 1., -1.]]
    scaler = MinMaxScaler()
    scaler.fit(x)
    print(scaler.transform(x))

    # (x - 최소값) / (최대값 - 최소값) # 전체 기준, min max scaler
    xx = np.array(x).reshape(-1)
    print(xx)
    min_x = np.min(xx)
    max_x = np.max(xx)
    yy = (xx - min_x) / (max_x - min_x)
    print(yy.reshape(3,3))

