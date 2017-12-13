# Day_03_05_sklearn.py

# scikit-learn, sklearn
from sklearn import datasets, svm, random_projection, preprocessing, model_selection
from sklearn.multiclass import OneVsOneClassifier

import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix

def not_used01():
    iris = datasets.load_iris()
    print(type(iris))               # Bunch, dictionary like # dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names'])
    print(iris.keys())

    print(iris['target_names'])     # ['setosa' 'versicolor' 'virginica']
    print(iris['data'])
    print(iris['target'])
    print(iris['feature_names'])    # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    print(iris['DESCR'])            # dataset에 대한 설명

    print(type(iris['data']))       # numpy.ndarray

def outline(number) :
    number = number.reshape(-1, 8)

    for row in number:
        for col in row:
            print(1 if col > 5 else ' ', end=' ')
        print()

def not_used02():
    digits = datasets.load_digits()
    print(digits.keys())                # dict_keys(['data', 'target', 'target_names', 'images', 'DESCR'])

    print(digits.data)
    print(digits.data.shape)            # (1797, 64)
    print(digits.data[0].reshape(-1, 8))

    print(digits.target[0])

    for i in range(10) :
        outline(digits.data[i])
        print(digits.target[i])
        print('-' * 50)

    print(digits.images.shape)
    print(digits.data.shape)

def not_used03():
    digits = datasets.load_digits()
    clf = svm.SVC(gamma=0.001, C=100)                           # SVM support vector machine
    fit = clf.fit(digits.data[:-1], digits.target[:-1])

    pred = clf.predict(digits.data[-1:])
    print(pred)
    print(digits.target[-1])

    #-----------------------------------------------------------------#
    # pickle 을 이용해서 저장 가능
    print('-' * 50)
    s = pickle.dumps(clf)
    clf2 = pickle.loads(s)
    print(clf2)
    print(clf2.predict(digits.data[-1:]))

def not_used04():
    digits = datasets.load_digits()
    train_count = int(len(digits.data) * 0.8)

    print(train_count)

    clf = svm.SVC(gamma=0.001, C=100)
    clf.fit(digits.data[:train_count], digits.target[:train_count])

    y_hat = clf.predict(digits.data[train_count:])
    label = digits.target[train_count:]

    np.set_printoptions(linewidth=1000)
    print(np.mean(y_hat == label))

def not_used05():
    # 문제
    # iris 데이터셋에 대해 SVC 객체를 생성해서
    # 전체 데이터에 학습한 다음에
    # 맨 앞에 있는 3개의 데이터에 대해서 검증해보세요.
    iris = datasets.load_iris()

    clf = svm.SVC(gamma=0.001, C=100)
    clf.fit(iris.data, iris.target)

    y_hat = clf.predict(iris.data[:3])
    label = iris.target[:3]

    print(iris.target_names[y_hat])
    # ---------------------------------------------------------------- #
    np.set_printoptions(linewidth=1000)
    print(np.mean(y_hat == label))

    clf.fit(iris.data, iris.target_names[iris.target])
    y_hat = clf.predict(iris.data[:3])
    print(y_hat)

def not_used06():
    digits = datasets.load_digits()

    data = model_selection.train_test_split(digits.data,            # data를 shuffle 해줌.
                                            digits.target,
                                            train_size=0.7)

    train_x, test_x, train_y, test_y = data
    print(train_x.shape, test_x.shape)          # (1257, 64) (540, 64)
    print(train_y.shape, test_y.shape)          # (1257,) (540,)

    data = model_selection.train_test_split(digits.data,            # data를 shuffle 해줌.
                                            digits.target,
                                            train_size=1300)

    train_x, test_x, train_y, test_y = data
    print(train_x.shape, test_x.shape)          # (1300, 64) (497, 64)
    print(train_y.shape, test_y.shape)          # (1300,) (497,)

    data = model_selection.train_test_split(digits.data,            # data를 shuffle 해줌.
                                            digits.target)

    train_x, test_x, train_y, test_y = data
    print(train_x.shape, test_x.shape)          # (1347, 64) (450, 64)
    print(train_y.shape, test_y.shape)          # (1347,) (450,)

    # 문제
    # train set에 대해서 학습하고, test set 에 대해서 결과를 예측
    clf = svm.SVC(gamma=0.001, C=100)
    clf.fit(train_x, train_y)
    y_hat = clf.predict(test_x)

    print(np.mean(y_hat == test_y))         # 정확도 계산
    print(clf.score(test_x, test_y))        # 정확도 계산, clf.score() 사용

# 문제
# iris를 DataFrame 객체에 저장한 다음에 그래프로 그려보세요.
iris = datasets.load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

# df.plot()
# scatter_matrix(df)
# scatter_matrix(df, c=iris.target)
scatter_matrix(df, c=iris.target, hist_kwds={'bins' : 20})          # 히스토그램 막대 개수
plt.show()