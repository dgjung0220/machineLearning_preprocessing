# Day_05_03_cross_validation.py

from sklearn import datasets, linear_model, model_selection
import numpy as np

def simple():
    # x, y = datasets.make_blobs(random_state=0)
    iris = datasets.load_iris()
    data = model_selection.train_test_split(iris.data, iris.target, random_state=0)
    train_x, test_x, train_y, test_y = data

    lr = linear_model.LogisticRegression()
    lr.fit(train_x, train_y)
    print('score : ', lr.score(test_x, test_y))         # score :  0.868421052632

def cross_validation():
    iris = datasets.load_iris()
    lr = linear_model.LogisticRegression()

    # default, 3회 검증(k-fold)
    scores = model_selection.cross_val_score(lr, iris.data, iris.target)
    print('3-folds :', scores)                                           # scores : [ 0.96078431  0.92156863  0.95833333]

    # 5회 검증
    scores = model_selection.cross_val_score(lr, iris.data, iris.target, cv=5)
    print('5-folds: ', scores)                                          # [ 1.          0.96666667  0.93333333  0.9         1.        ]
    print('mean', scores.mean())                                        # 96%

def k_fold():
    iris = datasets.load_iris()

    sp1 = model_selection.KFold()
    for train_index, test_index in sp1.split(iris.data, iris.target):
        print(len(train_index), len(test_index))
    print()

    sp2 = model_selection.KFold(n_splits=5)
    for train_index, test_index in sp2.split(iris.data, iris.target):
        print(len(train_index), len(test_index))
    print()

    sp3 = model_selection.KFold(n_splits=5)
    for train_index, test_index in sp3.split(iris.data, iris.target):
        print(train_index[:10]) # 이상함.. 선생님꺼 나중에 참고
    print()

def cv_detail():
    iris = datasets.load_iris()
    lr = linear_model.LogisticRegression()

    print(model_selection.cross_val_score(lr, iris.data, iris.target, cv=model_selection.KFold()))
    # [ 0.  0.  0.]

    print(model_selection.cross_val_score(lr, iris.data, iris.target, cv=model_selection.KFold(n_splits=5)))
    # [ 1.          0.93333333  0.43333333  0.96666667  0.43333333]

    print(model_selection.cross_val_score(lr, iris.data, iris.target, cv=model_selection.KFold(shuffle=True, random_state=0)))
    # [ 0.9   0.96  0.96]

    print(model_selection.cross_val_score(lr, iris.data, iris.target, cv=model_selection.KFold(shuffle=True, random_state=0, n_splits=5)))
    # [ 0.96666667  0.9         0.96666667  0.96666667  0.93333333]

    # 전체 데이터 개수대로 나누어버림
    # 데이터 개수가 작을 때 사용하는 방법 LeaveOneOut()
    loocv = model_selection.cross_val_score(lr, iris.data, iris.target, cv=model_selection.LeaveOneOut())
    print(loocv)
    print(len(loocv))
    loocv = model_selection.cross_val_score(lr, iris.data, iris.target, cv=model_selection.KFold(n_splits=150))
    print(loocv.mean())

def shuffle_split():
    iris = datasets.load_iris()

    sp1 = model_selection.ShuffleSplit(train_size=0.6, test_size=0.4, n_splits=3)
    for train_index, test_index in sp1.split(iris.data, iris.target):
        print(len(train_index), len(test_index))
    print()

    sp2 = model_selection.ShuffleSplit(train_size=0.6, n_splits=3)
    for train_index, test_index in sp2.split(iris.data, iris.target):
        print(len(train_index), len(test_index))
    print()

    sp3 = model_selection.ShuffleSplit(test_size=0.4, n_splits=3)
    for train_index, test_index in sp3.split(iris.data, iris.target):
        print(len(train_index), len(test_index))
    print()

    total = []
    sp4 = model_selection.ShuffleSplit(train_size=100, test_size=50, n_splits=3)
    for train_index, test_index in sp4.split(iris.data, iris.target):
        print(len(test_index), test_index[:10])
        total += list(test_index)

    print(sorted(total))

def group_kfold():
    lr = linear_model.LogisticRegression()
    x, y = datasets.make_blobs(n_samples=12, random_state=0)

    print(x)
    print(y)

    # groups!? 모호함
    groups = [0,0,0,1,1,1,1,2,2,3,3,3]
    scores = model_selection.cross_val_score(lr, x, y, groups, cv=model_selection.GroupKFold(n_splits=3))
    print(scores)
    print('-' * 50)

    sp1 = model_selection.GroupKFold()
    for train_index, test_index in sp1.split(x,y, groups):
        print(train_index, test_index)
    print()

    sp2 = model_selection.GroupKFold(n_splits=4)
    for train_index, test_index in sp2.split(x, y, groups):
        print(train_index, test_index)
    print()
