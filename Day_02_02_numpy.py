# Day_02_02_numpy.py

import numpy as np

a = np.array([1,3,5])
b = np.array([2,4,6])

print(a + 3)                # broadcasting
print(a + b)                # data의 개수만큼 연산이 발생. # vector operation
print(a * b)                # element-wise 곱
print('-' * 50)

# 문제
# 아래 배열은 몇 행 몇 열입니까.
a = np.array([0, 1, 2])                     # (3,)
b = np.array([0, 1, 2, 3, 4, 5])            # (6,)
c = np.array([[0, 1, 2]])                   # (1, 3)
d = np.array([[0, 1, 2], [3, 4, 5]])        # (2, 3)
e = np.array([[0], [1], [2]])               # (3, 1)

# print(a + b)                              # error # data의 갯수가 맞지 않다.
print(a + c)                                # 차원은 다르지만 data의 갯수가 같다.
print(a + d)                                # data 의 갯수가 같으므로 한 줄씩 더한다.  # broadcasting(수직)
print(a + e)                                # broadcasting(수직/수평)
print('-' * 50)

# print(b + c)                              # error
# print(b + d)                              # error
print(b + e)                                # broadcasting
print(c + d)
print(c + e)
# print(d + e)                              # error
print('-' * 50)

np.random.seed(12)                          # 난수 seed 값
print(np.random.rand(2, 3))                 # numpy random 2행 3열로 random 생성
print(np.random.randint(10))                # 10보다 작은 난수

a = np.arange(10, 20 , 2)
print(a)
print(np.random.choice(a))                  # 가지고 있는 값 중에서 선택.
print(np.random.choice(a, 7))               # 중복 허용해서 7개 생성
print('-' * 50)

b = np.arange(12).reshape(-1, 4)
print(b)
print(b.sum())
print(np.sum(b))
print(np.sum(b, axis=0))                    # 수직 (열, column)
print(np.sum(b, axis=1))                    # 수평 (행, row)
print('-' * 50)

def func(row, col):
    return row * 10 + col

a1 = np.fromfunction(func, shape=[5, 4], dtype=np.int32)                        # fromfunction, 함수를 이용하여 만들기.
a2 = np.fromfunction(lambda r, c: r*10 + c, shape=[5,4], dtype=np.int32)        # lambda 표현
print(a1)
print(a2)
print('-' * 50)

print(a2[0])
print(a2[0][0])             # print(a2[0, 0]) 과 동일  # fancy indexing
# 문제
# 마지막 데이터를 출력해 보시오.
print(a2[-1][-1])           # print(a2[-1, -1]) 과 동일
print(a2[::-1])             # 행 거꾸로 출력
print(a2[::-1,::-1])        # 모두 거꾸로 출력
print('-' * 50)

# 문제
# 행과 열을 바꿔서 출력해 보세요. (반복문 사용)
for i in a2[0]:
    print(a2[:,i])
print('-' * 50)

c = np.array([[1,2,3], [4,5,6]])
print(c)
c[0] = 0                    # 0행의 모든 데이터 변경
print(c)
c[:,0] = 99                 # 0열의 모든 데이터 변경
print(c)
print('-' * 50)

d = np.arange(3, 9)
print(d)
i = [1, 3, 4, 1]            
print(d[i])                 # index 배열
print(d[[1, 3, 4, 1]])

# 문제
# 대각선이 1로 채워진 5x5 행렬을 만드세요.
# 나머지는 0
print(np.eye(5, 5, dtype=np.int32))

temp = np.zeros((5,5), dtype=np.int32)
temp[range(5), range(5)] = 2
print(temp)

# 문제
# 테두기가 1로 채워진 5x5 배열을 만드세요.
temp = np.zeros((5,5), dtype=np.int32)
# temp[0, range(5)] = 1
# temp[-1, range(5)] = 1
# temp[range(5), 0] = 1
# temp[range(5), -1] = 1
# print(temp)

temp[[0, -1]] = 1
temp[:, [0,-1]] = 1
print(temp)
print('-' * 50)

g = np.ones([5,5], dtype=np.int32)
g[1:-1 , 1: -1] = 0
print(g)
print('-' * 50)

a = np.array([8, 1, 5])
print(a)
print(np.argsort(a))            # [1 2 0] # sort 된 index 결과를 리턴

b = np.argsort(a)               # index sort
print(a[b])                     # [1 5 8]

# 문제
# 어떤 순서로 값이 출력될까요
x = np.array([4, 3, 1, 5 ,2])
print(np.argsort(x))            # 2 4 1 0 3