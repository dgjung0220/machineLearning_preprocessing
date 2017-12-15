# Day_05_06_grid_search_leaf.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection, preprocessing, svm

# 문제
# leaf.csv 파일을 사용해서
# svm을 적용한 그리드서치 + 교차 검증을 구현해 보세요.

def grid_search_cv(train_x, test_x, train_y, test_y):
    # ---------------------------------------------------------- #
    scaler = preprocessing.StandardScaler().fit(train_x)
    train_x = scaler.transform(train_x)
    test_x = scaler.transform(test_x)
    # ---------------------------------------------------------- #
    param_range = np.geomspace(0.001, 100, 6)

    best_score, beast_param = 0, {}
    for gamma in param_range:
        for C in param_range:
            clf = svm.SVC(gamma=gamma, C=C)
            scores = model_selection.cross_val_score(clf, train_x, train_y, cv=3)

            if best_score < scores.mean():
                best_score = scores.mean()
                best_param = {'gamma': gamma, 'C': C}

    clf = svm.SVC(gamma=best_param['gamma'], C=best_param['C'])
    clf.fit(train_x, train_y)
    score = clf.score(test_x, test_y)

    print('     score :' , score)
    print('best score : ', best_score)
    print('best param : ', best_param)

    return score, best_score, best_param

path = 'Data/leaf.csv'
leaf = pd.read_csv(path, index_col=0)

x = leaf.drop('species', axis = 1)
y = preprocessing.LabelEncoder().fit_transform(leaf.species)
data = model_selection.train_test_split(x, y, random_state=0)
train_x, test_x, train_y, test_y = data

scores, best_scores, param_grid = grid_search_cv(*data)
# draw_heatmap([1,1,1], param_grid)