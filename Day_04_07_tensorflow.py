# Day_04_07_tensorflow.py

from sklearn import linear_model, model_selection
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

np.set_printoptions(linewidth=200)

def make_wave(n_samples):
    rnd = np.random.RandomState(42)                             # 메르센 소수 이용한 random state

    x = rnd.uniform(-3, 3, size=n_samples)

    noise = np.sin(4 * x) + x
    y = (noise + rnd.normal(size=len(x))) / 2

    # plt.plot(x, y, 'ro')
    # plt.plot([-3,3], [-2,2])
    # plt.show()
    return x.reshape(-1, 1), y

def regression_scikit(train_x, test_x, train_y, test_y):
    lr = linear_model.LinearRegression()
    lr.fit(train_x, train_y)

    print('[scikit]')
    print('{}, {}'.format(lr.coef_[0], lr.intercept_))          # 0.39390555116733955, -0.031804343026759746(W, b)

    print('train : ', lr.score(train_x, train_y))
    print('test : ', lr.score(test_x, test_y))

def regression_tensor(train_x, test_x, train_y, test_y):

    def score(sess, hypothesis, x_holder, x_data, y_data):
        y_hat = sess.run(hypothesis, feed_dict={x_holder: x_data})

        y_mean = np.mean(y_data)
        u = np.sum((y_hat - y_data) ** 2)
        v = np.sum((y_mean - y_data) ** 2)

        return 1 - u / v

    train_x = train_x.reshape(-1)
    train_y = train_x.reshape(-1)

    x = tf.placeholder(tf.float32)
    w = tf.Variable(tf.random_uniform([1], -1, 1))
    b = tf.Variable(tf.random_uniform([1], -1, 1))

    hypothesis = w*x + b;
    cost = tf.reduce_mean((hypothesis - train_y) ** 2)

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(cost)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(100):
        sess.run(train, feed_dict={x: train_x})

    print('[tensor]')
    print('{}, {}'.format(sess.run(w), sess.run(b)))

    print('train : ', score(sess, hypothesis, x, train_x, train_y))
    print('test : ', score(sess, hypothesis, x, test_x, test_y))

    sess.close()

x, y = make_wave(60)
print(x.shape, y.shape)         # (60, 1) (60,)

data = model_selection.train_test_split(x, y, random_state=42)
train_x, test_x, train_y, test_y = data

regression_scikit(train_x, test_x, train_y, test_y)
regression_scikit(*data)                                # 위, 아래 둘 다 가능

regression_tensor(train_x, test_x, train_y, test_y)