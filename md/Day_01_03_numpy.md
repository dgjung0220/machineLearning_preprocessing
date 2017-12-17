### Numpy

>Numarray와 Numeric이라는 오래된 Python 패키지를 계승해서 나온 수학 및 과학 연산을 위한 파이썬 패키지이다.  
>프로그래밍 하기 어려운 C,C++,Fortran[1] 등의 저수준 언어에 비하면, NumPy로는 꽤나 편리하게 수치해석을 실행할 수 있다. 게다가 Numpy 내부는 상당부분 C나 포트란으로 작성되어 실행 속도도 꽤 빠른편이다. 기본적으로 array라는 자료를 생성하고 이를 바탕으로 색인, 처리, 연산 등을 하는 기능을 수행한다. 물론 넘파이 자체만으로도 난수생성, 푸리에변환, 행렬연산, 간단한 기술통계 분석 정도는 가능하지만 실제로는 Scipy, Pandas, matplotlib 등 다른 Python 패키지와 함께 쓰이는 경우가 많다.  
>파이썬으로 수치해석, 통계 관련 기능을 구현한다고 할 때 Numpy는 가장 기본이 되는 모듈이다. 그만큼 Numpy는 수치해석/ 통계 관련 작업시 중요한 역할을 하므로, 파이썬으로 관련 분야에 도전하고자 한다면 반드시 이에 대한 기초를 잘 쌓아두고 가자.-[나무위키](https://namu.wiki/w/NumPy)

#### Numpy 기본
np.arange 는 매개 변수의 숫자-1 만큼의 배열(ndarray) 를 생성한다. 파이썬은 본래 배열이 없지만 numpy를 이용하면 배열을 사용할 수 있다.
```python
import numpy as np              

a = np.arange(5)
print(a)                        # [0 1 2 3 4] 
print(type(a))                  # numpy.ndarray(n-dimesion array)
```

numpy의 배열은 shape 로 형태를 확인할 수 있고, reshape 을 이용하여 배열 차원을 재정의할 수 있다.
```python
a1 = np.arange(10)
a2 = np.arange(15)
a3 = np.arange(20)

print(a1.shape, a1.dtype)               # (10,) int32
print(a2.shape, a2.dtype)               # (15,) int32
print(a3.shape, a3.dtype)               # (20,) int32

a2 = np.arange(15).reshape(3, 5)
a3 = np.arange(20).reshape(2, 2, 5)

print(a2.shape, a2.dtype)               # (3, 5) int32
# print(a3.shape, a3.dtype)             # (2, 2, 5) int32
```
아래 코드를 보면 파이썬의 리스트와 numpy의 배열은 출력 결과가 다르다. numpy 배열은 list()로 변환할 수 있다.
```python
print([1,3, 5])                         # [1, 3, 5]
print(np.array([1, 3, 5]))              # [1 3 5]
print(list(np.array([1, 3, 5])))        # [1, 3, 5]
```    

#### 0~5 사이의 숫자가 포함된 2행 3열 크기의 배열을 만들기
```python
print(np.array([0,1,2,3,4,5]).reshape(2,3))
print(np.array([[0,1,2],[3,4,5]]))
print(np.array([range(3),range(3,6)]))
print(np.arange(6).reshape(2,3))
```
```python
print(np.arange(6).reshape(-1,3))           # -1 값 전달로 알아서 계산.
print(np.arange(6).reshape(2,-1))
```

```python
# 문제
# 아래의 2차원 배열을 1차원으로 변환해 보세요.
    
a = np.arange(6).reshape(2, 3)
print(a.reshape(6))
print(np.reshape(a, 6))
print(a.reshape(a.size))
print(a.reshape(-1))
```

#### zeros, ones, full, zeros_like
```python
print(np.zeros([2, 3]))
print(np.ones([2, 3]))
print(np.full([2,3], -1))                   # -1 로 채우기 '-1' 자리에 모든 수 가능.

a = np.arange(6).reshape(2, 3)
print(np.zeros_like(a, dtype=np.float32))   # a와 같은 shape 로 생성
print(np.zeros(a.shape, dtype=np.int32))
```

#### arange, linspace
```python
print(np.arange(0, 2, 0.25))                # 0~2 사이 0.25 간격으로 배열 생성
print(np.linspace(0, 2, 9))                 # 0~2 사이에 길이 9인 배열 생성
```

#### 배열 브로드캐스팅
```python
a = np.array([0,1,2])
a += 1                                      
print(a)                                    # [1 2 3]
print(a ** 2)                               # [1 4 9]
print(a > 1)                                # [False True True]
print(a[a>1])                               # 1보다 큰 것들만 출력 # [2 3]
```

#### Universal function
```python
print(np.sin(a))                            # Universal function
```

배열의 차원과 무관하게 Broadcasting, Universal function이 적용된다.
```python
b = np.arange(6).reshape(-1,3)
print(b)
print(b + 1)
print(b ** 2)
print(b > 1)
print(b[b>1])
```

#### 행렬 곱 : np.dot()
```python
c = np.arange(6).reshape(-1,3)

test1 = np.arange(4).reshape(-1,2)
test2 = np.arange(6).reshape(-1,2)
test3 = np.arange(8).reshape(-1,2)
print(np.dot(test1, c))
print(np.dot(test2, c))
print(np.dot(test3, c))
```

#### 전치 행렬 : transpose()
```python
print(c.transpose())
print(c.T)
print(np.dot(c, c.T))
```

#### Slicing
```python
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]          
print(a[0], a[1])                           # 0 1
print(a[len(a)-1], a[len(a)-2])             # 9 8
print(a[-1], a[-2])                         # 9 8

print(a[3:7])                               # slicing (range 와 동일하게 동작함)

# 앞쪽 절반을 출력
print(a[:int(len(a)/2)])                    # [0, 1, 2, 3, 4]
# 뒤쪽 절반을 출력
print(a[int(len(a)/2):])                    # [5, 6, 7, 8, 9]

# 짝수 번째만 출력
print(a[::2])                               # [0, 2, 4, 6, 8]
# 홀수 번째만 출력
print(a[1::2])                              # [1, 3, 5, 7, 9]

# 거꾸로 출력
print(a[::-1])                              # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```
