### Numpy 2차

#### Vector Operation
배열끼리의 연산은 배열 내 인덱스의 개수만큼 연산이 발생한다.
```python
import numpy as np

a = np.array([1,3,5])
b = np.array([2,4,6])

print(a + 3)            # [4 6 8] # broadcasting
print(a + b)            # Vector Operation # [3 7 11]
```

#### 다차원 배열
```python
import numpy as np

a = np.array([0, 1, 2])                     # (3,)
b = np.array([0, 1, 2, 3, 4, 5])            # (6,)
c = np.array([[0, 1, 2]])                   # (1, 3)
d = np.array([[0, 1, 2], [3, 4, 5]])        # (2, 3)
e = np.array([[0], [1], [2]])               # (3, 1)

# print(b + c)                              # error # 서로 다른 shape 더하기 연산.
# print(b + d)                              # error

print(b + e)                                # broadcasting
                                            # [[0 1 2 3 4 5]
                                            #  [1 2 3 4 5 6]
                                            #  [2 3 4 5 6 7]]

print(c + d)                                # [[0 2 4]
                                            #  [3 5 7]]
                                            
print(c + e)                                # [[0 1 2] 
                                            #  [1 2 3] 
                                            #  [2 3 4]]
                                            
# print(d + e)                              # error
```
#### Random
```python
import numpy as np

np.random.seed(12)                          # 난수 seed
print(np.random.rand(2,3))                  # 2행 3열의 random 배열 생성
                                            # [[ 0.15416284  0.7400497   0.26331502]
                                            #  [ 0.53373939  0.01457496  0.91874701]]

print(np.random.randint(10))                # 10보다 작은 난수 생성 # 6
```
#### Random choice
```python
import numpy as np

a = np.arange(10, 20, 2)                    # [10 12 14 16 18]
print(np.random.choice(a))                  # 가지고 있는 값 중에서 임의의 값 하나를 선택.
print(np.random.choice(a, 7))               # 가지고 있는 값 중에서 임의의 7개 값을 선택. # 중복 허용

b = np.arange(12).reshape(-1,4)             # 3행 4열
print(b.sum())                              # 66, python sum
print(np.sum(b))                            # 66, numpy sum
print(np.sum(b, axis=0))                    # 수직 sum (column) # [12 15 18 21]
print(np.sum(b, axis=1))                    # 수평 sum (row)    # [ 6 22 38]
```

#### fromfunction & lamda
특이한 점은 함수를 정의하여, 배열 생성시 이용할 수 있다는 점이다. 함수의 자리는 lamda 식으로 대체할 수 있다.
```python
def func(row, col):
    return row * 10 + col

a1 = np.fromfunction(func, shape=[5, 4], dtype=np.int32)                        # fromfunction, 함수를 이용하여 만들기.
a2 = np.fromfunction(lambda r, c: r*10 + c, shape=[5,4], dtype=np.int32)        # lambda 표현

# 마지막 데이터의 출력
print(a2[-1][-1])                           # print(a2[-1, -1]) 과 동일
print(a2[::-1])                             # 행 거꾸로 출력
print(a2[::-1,::-1])                        # 모두 거꾸로 출력 # fancy indexing

# 행과 열을 바꿔서 출력
for i in a2[0]:
    print(a2[: , i])
```

#### 여러 가지 배열 인덱싱 
```python
c = np.array([[1,2,3], [4,5,6]])
c[0] = 0                                    # 0행의 모든 데이터 변경
c[:,0] = 99                                 # 0열의 모든 데이터 변경

d = np.arange(3, 9)                         # [3 4 5 6 7 8]
i = [1, 3, 4, 1]            
print(d[i])                                 # index를 이용한 배열 # [4 6 7 4]
print(d[[1, 3, 4, 1]])
```

#### 단위 행렬
np.eye() 함수를 이용하여 단위 행렬을 만들 수 있다. 단위 행렬은 대각선이 1이고 나머지가 0인 정사각 행렬이다.
```python
import numpy as np

print(np.eye(5, 5, dtype=np.int32))

# 직접 만들기
temp = np.zeros((5,5), dtype=np.int32)
temp[range(5), range(5)] = 1

# 번외, 테두리가 1로 채워진 5x5 배열
# method 1. 
temp = np.zeros((5,5), dtype=np.int32)
temp[[0,-1]] = 1                            # 0행과 마지막 행 1
temp[:, [0,-1]] = 1                         # 0열과 마지막 열 1

# method 2.
temp = np.ones((5,5), dtype=np.int32)
temp[1:-1, 1:-1] = 0
```

#### argsort
```python
import numpy as np

a = np.array([8, 1, 5])                     # [8 1 5]
print(np.argsort(a))                        # [1 2 0]   # sort 된 이 전 index 의 결과를 리턴

b = np.argsort(a)
print(a[b])                                 # [1 5 8]
```