# Day_05_05_grid_search.py

from sklearn import datasets, svm, model_selection
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width', 1000)

def simple_grid_search(train_x, test_x, train_y, test_y):

    best_score, best_param = 0, {}
    for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
        for C in [0.001, 0.01, 0.1, 1, 10, 100]:
            clf = svm.SVC(gamma=gamma, C=C)
            clf.fit(train_x, train_y)

            score = clf.score(test_x, test_y)
            # print(score)

            if best_score < score :
                best_score = score
                best_param = {'gamma' : gamma, 'C' : C}

    print('best score : ', best_score)
    print('best param : ', best_param)
    # best score: 0.973684210526
    # best score: {'gamma': 0.001, 'C': 100}

# valid dataset 의 튜닝
def better_grid_search(total_x, test_x, total_y, test_y):
    data = model_selection.train_test_split(total_x, total_y, random_state=0)
    train_x, valid_x, train_y, valid_y = data
    # print(train_x.shape, valid_x.shape, test_x.shape)
    # (84, 4) (28, 4) (38, 4)

    best_score, best_param = 0, {}
    for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
        for C in [0.001, 0.01, 0.1, 1, 10, 100]:
            clf = svm.SVC(gamma=gamma, C=C)
            clf.fit(train_x, train_y)

            score = clf.score(valid_x, valid_y)

            if best_score < score:
                best_score = score
                best_param = {'gamma': gamma, 'C': C}

    # 나머지 부분을 완성해보세요.
    # 검증까지 합니다.
    clf = svm.SVC(gamma=best_param['gamma'], C=best_param['C'])
    clf.fit(total_x, total_y)
    score = clf.score(test_x, test_y)

    print('     score :' , score)
    print('best score : ', best_score)
    print('best param : ', best_param)

def cv_grid_search(train_x, test_x, train_y, test_y):
    # 문제
    # cross validation 코드로 변환해보셍.

    best_score, best_param = 0, {}
    for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
        for C in [0.001, 0.01, 0.1, 1, 10, 100]:
            clf = svm.SVC(gamma=gamma, C=C)
            scores = model_selection.cross_val_score(clf, train_x, train_y, cv=5)

            if best_score < scores.mean():
                best_score = scores.mean()
                best_param = {'gamma': gamma, 'C': C}

    clf = svm.SVC(gamma=best_param['gamma'], C=best_param['C'])
    # clf = svm.SVC(**best_param)
    clf.fit(train_x, train_y)
    score = clf.score(test_x, test_y)

    print('     score :' , score)
    print('best score : ', best_score)
    print('best param : ', best_param)

def grid_search_cv(train_x, test_x, train_y, test_y):
    param_grid = {'gamma': [0.001, 0.01, 0.1, 1, 10, 100],
                  'C' : [0.001, 0.01, 0.1, 1, 10, 100]}

    grid_search = model_selection.GridSearchCV(svm.SVC(), param_grid=param_grid, cv=5)
    grid_search.fit(train_x, train_y)

    print('test score :', grid_search.score(test_x, test_y))
    print('best score :', grid_search.best_score_)
    print('best param :', grid_search.best_params_)
    # test score: 0.973684210526
    # best score: 0.973214285714
    # best param: {'C': 100, 'gamma': 0.01}

    return grid_search, param_grid

def draw_heatmap(scores, param_grid):
    ax = plt.gca()
    img = ax.pcolor(scores)
    img.update_scalarmapplable()

    ax.set_xlabel('gamma')
    ax.set_ylabel('C')
    ax.set_xticks(np.arange(6) + 0.5)
    ax.set_yticks(np.arange(6) + 0.5)
    ax.set_xticklabels(param_grid['gamma'])
    ax.set_yticklabels(param_grid['C'])
    ax.set_aspect(1)

    for p, color, value in zip(img.get_paths(), img.get_facecolors(), img.get_array()):
        x,y = p.vertices[:-2, :].mean(0)
        c = 'k' if np.mean(color[:3]) > 0.5 else 'w'
        ax.test(x, y, '{:2f}'.format(value), color=c, ha='center', va='center')

def bad_heatmap(train_x, train_y):
    param_linear = {'C': np.linspace(1, 2, 6), 'gamma': np.linspace(1,2,6)}
    param_onelog = {'C': np.linspace(1, 2, 6), 'gamma': np.logspace(-3,2,6)}
    param_range = {'C': np.logspace(-3, 2, 6), 'gamma': np.logspace(-7,2,6)}

    for i, param_grid in enumerate([param_linear, param_onelog, param_range]):
        grid_search = model_selection.GridSearchCV(svm.SVC(), param_grid, cv=5)
        grid_search.fit(train_x, train_y)

        scores = grid_search.cv_results_['mean_test_score'].reshape()

        plt.subplot(1, 3, i+1)
        draw_heatmap(scores, param_grid)

def cv_pandas_heatmap(train_x, test_x, train_y, test_y):
    grid_search, param_grid = grid_search_cv(train_x, test_x, train_y, test_y)
    results = pd.DataFrame(grid_search.cv_results_)
    # print(results)
    # print(results.T)
    scores = np.array(results.mean_test_score).reshape(6,6)
    print(scores)

    plt.figure(1)
    plt.figure(2, figsize=[12, 5])
    # draw_heatmap(scores, param_grid)
    bad_heatmap(train_x, train_y)

    plt.show()

def different_params(train_x, test_x, train_y, test_y):
    param_grid = [{'kernel': ['rbf'],
                   'C' : [0.001, 0.01, 0.1, 1, 10, 100]},
                  {'kernel': ['linear'],
                   'gamma' : [0.001, 0.01, 0.1, 1, 10, 100]}]

    grid_search = model_selection.GridSearchCV(svm.SVC(), param_grid=param_grid, cv=5)
    grid_search.fit(train_x, train_y)

    print('test score :', grid_search.score(test_x, test_y))
    print('best score :', grid_search.best_score_)
    print('best param :', grid_search.best_params_)


iris = datasets.load_iris()
data = model_selection.train_test_split(iris.data, iris.target, random_state=0)

# simple_grid_search(*data)
# better_grid_search(*data)
# cv_grid_search(*data)
# grid_search_cv(*data)
# cv_pandas_heatmap(*data)
different_params(*data)