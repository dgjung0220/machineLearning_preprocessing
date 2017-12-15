# Day_05_02_categorical.py

from sklearn import model_selection, preprocessing, linear_model
import numpy as np
import pandas as pd

pd.set_option('display.width', 1000)

def use_get_dummies():
    # 똑같은 더미 만들어 줌.
    print(pd.get_dummies(['a','b','c','a']))
    print(preprocessing.LabelBinarizer().fit_transform(['a','b','c','a']))

    df = pd.get_dummies(['a','b','c','a'])

    print(type(df))
    print(df.values)
    print('-' * 50)

    print(pd.get_dummies(['a','b', np.nan]))                    # LabelBinarizer()는 처리 못 함.
    print(pd.get_dummies(['a','b', np.nan], dummy_na=True))
    print('-' * 50)

    df = pd.DataFrame({'A' : ['a','b','a'],
                       'B' : ['b','a','c'],
                       'C' : [1, 2 , 3]})
    print(df)
    print(pd.get_dummies(df))
    print(pd.get_dummies(df, prefix=['c1', 'c2']))

# >50K, <=50K.
#
# age: continuous.
# workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
# fnlwgt: continuous.
# education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
# education-num: continuous.
# marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
# occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
# relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
# race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
# sex: Female, Male.
# capital-gain: continuous.
# capital-loss: continuous.
# hours-per-week: continuous.
# native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.

def not_used01():
    names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
    adult = pd.read_csv('Data/adult.txt', header=None, names=names, index_col=False)
    # print(adult)

    # 문제
    # 남여 숫자를 세어 보세요.
    print(adult.sex.value_counts())
    print('-' * 50)
    by_gender = adult.groupby(by='sex').size()
    print(by_gender)
    print('-' * 50)

    adult_small = adult[['age', 'workclass', 'education', 'occupation', 'sex', 'hours-per-week', 'income']]

    adult_dummy = pd.get_dummies(adult_small)
    print(adult_dummy.shape)
    print(adult_dummy.head())

    print(adult_dummy.columns)
    print(adult_dummy.columns.values)
    print('-' * 50)

    # x, y 데이터 구분
    adult_data = adult_dummy.values[:, :-2]
    adult_target = adult_dummy.values[:, -1:]
    # adult_data = adult_dummy.iloc[:, :-2]
    # adult_target = adult_dummy.iloc[:, -1]

    data = model_selection.train_test_split(adult_data, adult_target, random_state=0)
    train_x, test_x, train_y, test_y = data

    lr = linear_model.LogisticRegression()
    lr.fit(train_x, train_y)

    print('train : ', lr.score(train_x, train_y))
    print('test : ', lr.score(test_x, test_y))

def not_used02():
    names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship',
             'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
    adult = pd.read_csv('Data/adult.txt', header=None, names=names, index_col=False)

    age = preprocessing.LabelEncoder().fit_transform(adult.age)
    workclass = preprocessing.LabelEncoder().fit_transform(adult.workclass)
    education = preprocessing.LabelEncoder().fit_transform(adult.education)
    occupation = preprocessing.LabelEncoder().fit_transform(adult.occupation)
    sex = preprocessing.LabelEncoder().fit_transform(adult.sex)
    hours_per_week = preprocessing.LabelEncoder().fit_transform(adult['hours-per-week'])
    income = preprocessing.LabelEncoder().fit_transform(adult.income)

    adult_dummy = np.vstack([age, workclass, education, occupation, sex, hours_per_week, income])
    adult_dummy = adult_dummy.T
    adult_data = adult_dummy[:, :-1]
    adult_target = adult_dummy[:, -1]
    data = model_selection.train_test_split(adult_data, adult_target, random_state=0)

    train_x, test_x, train_y, test_y = data

    lr = linear_model.LogisticRegression()
    lr.fit(train_x, train_y)

    print('train : ', lr.score(train_x, train_y))
    print('test : ', lr.score(test_x, test_y))


not_used01()
not_used02()