# Day_02_03_matplotlib.py

import numpy as np
import matplotlib.pyplot as plt
import csv

def graph01():
    plt.plot([10, 20, 30, 40 ,50])
    plt.show()

def graph02():
    plt.plot([1,2,3,4], [1, 4, 9, 16], 'ro')        # ro 선 대신 특정 점 찍을 때
    plt.xlim(0, 5)
    plt.ylim(0, 20)
    plt.show()

def graph03():
    # 문제
    # x 범위가 -10 ~ 10일 때의 x^2에 대한 그래프를 그려보세요.
    a = np.arange(-10,10, 0.1)
    plt.plot(a, a**2)
    plt.show()

def graph04():
    x = np.linspace(-10, 10, 100)
    y = np.sin(x)

    #plt.plot(x, y)
    #plt.plot(x, y, 'rx')
    plt.plot(x, y, marker='x')
    plt.show()

def graph05():
    # 문제
    # 로그 곡선 4개를 하나의 피겨에 그려 보세요.
    fig, ax = plt.subplots()
    ax.grid(True)

    a = np.arange(0.01, 2, 0.01)

    plt.plot(a, np.log(a))
    plt.plot(a, -np.log(a))

    a2 = np.arange(0.01-2, 0, 0.01)

    plt.plot(a2, np.log(-a2))
    plt.plot(a2, -np.log(-a2))
    plt.show()

def graph06():
    def func(t):
        return np.exp(-t) * np.cos(2*np.pi * t)

    t1 = np.arange(0, 5 ,0.1)
    t2 = np.arange(0, 5 ,0.02)

    plt.figure(1)
    plt.subplot(2,1,1)
    plt.plot(t1, func(t1))
    plt.subplot(2,1,2)
    plt.plot(t2, func(t2))

    plt.figure(2)
    plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
    plt.show()

def graph07():
    # 문제
    # 로그 곡선 4 개를 2 개의 피겨에 그려 보세요.
    fig, ax = plt.subplots()
    ax.grid(True)

    fig = plt.figure(1)
    a = np.arange(0.01, 2, 0.01)
    plt.subplot(2,1,1)

    fig.gca().grid(True)
    plt.plot(a, np.log(a))
    plt.subplot(2, 1, 2)
    fig.gca().grid(True)
    plt.plot(a, -np.log(a))

    fig = plt.figure(2)
    a2 = np.arange(0.01-2, 0, 0.01)
    plt.subplot(2, 1, 1)
    fig.gca().grid(True)
    plt.plot(a2, np.log(-a2))
    plt.subplot(2, 1, 2)
    fig.gca().grid(True)
    plt.plot(a2, -np.log(-a2))
    plt.show()

