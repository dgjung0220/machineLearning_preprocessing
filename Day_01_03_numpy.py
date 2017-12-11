# Day_01_03_numpy.py

import numpy as np
import matplotlib
import pandas

def one():
    a = np.arange(5)
    print(a)
    print(type(a))       # numpy.ndarray(n-dimesion array)

    a1 = np.arange(10)
    a2 = np.arange(15)
    a3 = np.arange(20)
    print(a1.shape, a1.dtype)   # (10,) int32
    print(a2.shape, a2.dtype)   # (15,) int32
    print(a3.shape, a3.dtype)   # (20,) int32

    a2 = np.arange(15).reshape(3, 5)
    a3 = np.arange(20).reshape(2, 2, 5)
    print(a2.shape, a2.dtype)   # (3, 5) int32
    print(a3.shape, a3.dtype)   # (2, 2, 5) int32

    print(a1)
    print(a2)
    print(a3)
    print('-'* 50)

    print([1, 3, 5])
    print(np.array([1, 3, 5]))
    print(list(np.arange(1, 7, 2)))

    # 문제
    # np.array 함수를 사용해서 0~5 사이의 숫자가 포함된 2행 3열 크기의 배열을 만들어 보세요.
    print(np.array([0,1,2,3,4,5]).reshape(2,3))
    print(np.array([[0,1,2],[3,4,5]]))
    print(np.array([range(3),range(3,6)]))
    print(np.arange(6).reshape(2,3))
    # -1 값 전달로 알아서 계산.
    print(np.arange(6).reshape(-1,3))
    print(np.arange(6).reshape(2,-1))

    # 문제
    # 아래의 2차원 배열을 1차원으로 변환해 보세요.
    a = np.arange(6).reshape(2, 3)
    print(a.reshape(6))
    print(np.reshape(a, 6))
    print(a.reshape(a.size))
    print(a.reshape(-1))
    print('-' * 50)

    print(np.zeros([2, 3]))
    print(np.ones([2, 3]))
    print(np.full([2,3], -1)) # -1 로 채우기 -1 자리에 모든 수 가능.

    a = np.arange(6).reshape(2, 3)
    print(np.zeros_like(a, dtype=np.float32))
    print(np.zeros(a.shape, dtype=np.int32))
    print('-' * 50)

    print(np.arange(0, 2, 0.25))
    print(np.linspace(0, 2, 9))

a = np.array([0,1,2])
a += 1                             # broadcasting
print(a)
print(a ** 2)
print(a > 1)
print(a[a>1]) # 1보다 큰 것들만 출력

print(np.sin(a))                  # Universal function

# 차원과 무관하게 broadcasting, Universal function 적용됨.
b = np.arange(6).reshape(-1,3)
print(b)
print(b + 1)
print(b ** 2)
print(b > 1)
print(b[b>1])
print('-' * 50)

# 행렬 곱 : np.dot()
# C와 행렬 곱셈이 성립되는 배열을 2개 만들어보세요.
c = np.arange(6).reshape(-1,3)

test1 = np.arange(4).reshape(-1,2)
test2 = np.arange(6).reshape(-1,2)
test3 = np.arange(8).reshape(-1,2)
print(np.dot(test1, c))
print(np.dot(test2, c))
print(np.dot(test3, c))

# 전치 행렬 : transpose()
print(c.transpose())
print(c.T)
print(np.dot(c, c.T))
print('-'* 50)

# Slicing
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[0], a[1])
print(a[len(a)-1], a[len(a)-2])
print(a[-1], a[-2])            # python

print(a[3:7])                  # slicing (range 와 동일하게 동작함)

# 문제
# 앞쪽 절반을 출력
print(a[:int(len(a)/2)])
# 뒤쪽 절반을 출력
print(a[int(len(a)/2):])

# 문제
# 짝수 번째만 출력
print(a[::2])
# 홀수 번째만 출력
print(a[1::2])

# 문제
# 거꾸로 출력해보세요
print(a[::-1])
