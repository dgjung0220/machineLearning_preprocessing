# Day_04_06_scaling_svm.py

from sklearn import svm, model_selection, datasets, preprocessing
from sklearn.preprocessing import (add_dummy_feature, Binarizer, Imputer, LabelBinarizer, LabelEncoder, MaxAbsScaler, MinMaxScaler)

from sklearn.preprocessing import (StandardScaler, MinMaxScaler, RobustScaler, MaxAbsScaler)

cancer = datasets.load_breast_cancer()

data = model_selection.train_test_split(cancer.data, cancer.target, random_state=42)
train_x, test_x, train_y, test_y = data
print(train_x.shape, test_x.shape)              # (426, 30) (143, 30)
print(train_y.shape, test_y.shape)              # (426,) (143,)

clf = svm.SVC(C=100)
clf.fit(train_x, train_y)
print('original : ', clf.score(test_x, test_y)) # original :  0.65034965035

# 문제
# MinMaxScaler를 사용해서 앞의 코드를 다시 적용.
scaler = MinMaxScaler()                         # preprocessing.MinMaxScaler
scaler.fit(train_x)

train_x_scaled = scaler.transform(train_x)
test_x_scaled = scaler.transform(test_x)

clf = svm.SVC(C=100)
clf.fit(train_x_scaled, train_y)
print('MinMax Scaler : ', clf.score(test_x_scaled, test_y))

# 문제
# Standard Scaler, MinMax, robust, MaxAbs
scaler = StandardScaler()
scaler.fit(train_x)
train_x_scaled = scaler.transform(train_x)
test_x_scaled = scaler.transform(test_x)

clf.fit(train_x_scaled, train_y)
print('Standard Scaler : ', clf.score(test_x_scaled, test_y))

#########################################################################
scaler = RobustScaler()
scaler.fit(train_x)
train_x_scaled = scaler.transform(train_x)
test_x_scaled = scaler.transform(test_x)

clf.fit(train_x_scaled, train_y)
print('Robust Scaler : ', clf.score(test_x_scaled, test_y))

scaler = MaxAbsScaler()
scaler.fit(train_x)
train_x_scaled = scaler.transform(train_x)
test_x_scaled = scaler.transform(test_x)

clf.fit(train_x_scaled, train_y)
print('MaxAbs Scaler : ', clf.score(test_x_scaled, test_y))