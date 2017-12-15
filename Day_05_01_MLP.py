# Day_05_01_MLP.py
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid import make_axes_locatable
from sklearn import datasets, model_selection, neural_network

cancer = datasets.load_breast_cancer()

print(cancer.keys())            # dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names'])
print(cancer.target)            # y data
print(cancer.data.shape)        # (569, 30)

data = model_selection.train_test_split(cancer.data, cancer.target)
train_x, test_x, train_y, test_y = data

# MLP : Multi-Layer Perceptron
mlp1 = neural_network.MLPClassifier(random_state=42)
mlp1.fit(train_x, train_y)

print('train : ', mlp1.score(train_x, train_y))
print('train : ', mlp1.score(test_x, test_y))
print()
# train :  0.915492957746
# train :  0.853146853147

# StandardScaler()
mean_on_train = train_x.mean(axis=0)
std_on_train = train_x.std(axis=0)

train_x_scaled = (train_x - mean_on_train) / std_on_train
test_x_scaled = (test_x - mean_on_train) / std_on_train

mlp2 = neural_network.MLPClassifier(random_state=42)
mlp2.fit(train_x_scaled, train_y)

print('train : ', mlp2.score(train_x_scaled, train_y))
print('test : ', mlp2.score(test_x_scaled, test_y))
print()
# train :  0.995305164319
# test :  0.965034965035

mlp3 = neural_network.MLPClassifier(random_state=42, max_iter=1000)         # max_iter, default = 200
mlp3.fit(train_x_scaled, train_y)

print('train : ', mlp3.score(train_x_scaled, train_y))
print('test : ', mlp3.score(test_x_scaled, test_y))
print('alpha : ', mlp3.alpha)
print('iter : ', mlp3.max_iter)
print()
# train :  0.995305164319
# test :  0.986013986014

mlp4 = neural_network.MLPClassifier(random_state=42, max_iter=1000, alpha=1)        # alpha, default = 0.0001
mlp4.fit(train_x_scaled, train_y)

print('train : ', mlp4.score(train_x_scaled, train_y))
print('test : ', mlp4.score(test_x_scaled, test_y))
print('alpha : ', mlp4.alpha)
print('iter : ', mlp4.max_iter)
print()
# train :  0.988262910798
# test :  0.986013986014

print(len(mlp4.coefs_))         # coefs_ 가중치
print(len(mlp4.coefs_[0]))      # 30, Weight
print(len(mlp4.coefs_[1]))      # 100, Bias
print(mlp4.coefs_[0].shape)     # (30, 100)
print(mlp4.coefs_[1].shape)     # (100, 1)
print('-' * 50)

# ------------------------------------------------------------------------------------------------------------------ #

plt.figure(figsize=[20,5])
ax = plt.gca()
im = ax.imshow(mlp4.coefs_[0])          # Weight 를 시각화
plt.yticks(range(30), cancer.feature_names)
plt.xlabel('hidden units')

divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='2%', pad=0.1)

plt.colorbar(im, cax)
plt.tight_layout()
plt.show()