# Day_04_09_leaf.py

import numpy as np
import pandas as pd
from sklearn import svm, model_selection, linear_model, neighbors, discriminant_analysis, preprocessing

pd.options.display.width = 1000
np.set_printoptions(linewidth=1000)

path = 'Data/leaf.csv'

def not_used():
    # svm, linear regression, knn
    # 문제
    # leaf.csv 파일을 사용해서
    # 위의 3가지 알고리즘으로 학습하고 검증


    leafs = pd.read_csv(path, index_col=0)

    x = leafs.drop('species', axis=1)
    y = preprocessing.LabelEncoder().fit_transform(leafs.species)

    data = model_selection.train_test_split(x, y, random_state=42)
    train_x, test_x, train_y, test_y = data

    clf = [svm.SVC(C=100), linear_model.LinearRegression(), neighbors.KNeighborsClassifier(), discriminant_analysis.LinearDiscriminantAnalysis()]

    for _ in clf:
        _.fit(train_x, train_y)
        print('. :', _.score(test_x, test_y))

def show_accuracy(train_x, test_x, train_y, test_y, classifiers):
    print('-' * 50)

    for clf in classifiers:
        clf.fit(train_x, train_y)
        acc = clf.score(test_x,  test_y)
        print('{:>30}: {}'.format(clf.__class__.__name__, acc))


leafs = pd.read_csv(path, index_col=0)

x = leafs.drop('species', axis=1)
y = preprocessing.LabelEncoder().fit_transform(leafs.species)

data = model_selection.train_test_split(x, y, random_state=42)
train_x, test_x, train_y, test_y = data

clf = [svm.SVC(C=100), linear_model.LinearRegression(), neighbors.KNeighborsClassifier(), discriminant_analysis.LinearDiscriminantAnalysis()]

sess = model_selection.StratifiedShuffleSplit(n_splits=5, test_size=0.2)

for train_index, test_index in sess.split(x, y) :
    train_x, test_x = x.values[train_index], x.values[test_index]
    train_y, test_y = y[train_index], y[test_index]

    show_accuracy(train_x, test_x, train_y, test_y, clf)