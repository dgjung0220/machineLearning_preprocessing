### Python 기본 문법
machine learning을 위한 tensorflow, scikit-learn 등을 다루기 위해 파이썬 기본 문법을 파악해야한다.

---
* 파이썬 관련 도서
    * (기본)[Try! helloworld 파이썬](http://www.yes24.com/24/Goods/35907623?Acode=101) 
    * (실력)[파이썬 코딩의 기술](http://www.yes24.com/24/goods/25138160?scode=032&OzSrank=1)
    * (분석-NumPy,pandas)[파이썬 라이브러리를 활용한 데이터 분석](http://www.hanbit.co.kr/store/books/look.php?p_code=B6540908288)
    * (분석-Scikitlearn)[파이썬 라이브러리를 활용한 머신러닝](http://www.hanbit.co.kr/store/books/look.php?p_code=B6119391002)
    * (딥러닝)[파이썬을 이용한 머신러닝, 딥러닝 실전 개발 입문](http://www.yes24.com/24/Goods/42496558?Acode=101)
--- 

#### 변수 타입
파이썬 기본 데이터 타입은 아래 네 가지(int, float, bool, str)가 있다.
```python
print(type(12), type(3.14), type(True), type('hello') )
```

결과 :
```
<class 'int'> <class 'float'> <class 'bool'> <class 'str'>
```

#### 문자, 타입 변환
숫자 문자열을 int, float 로 변환할 수 있다.
```
a = '123'
print(a. type(a))       # <class 'str'>
```
```
a = int(a)
print(type(a))          # <class 'int'>
```
```
a = float(a)
print(type(a))          # <class 'float'>
```

#### python 의 다중 치환
python은 아래와 같이 다중 치환이 가능하다. 다중 치환이 가능한 이유는 파이썬의 튜플(tuple) 덕분이다.
```python
a,b = 3, 7
print(a,b)
```
위의 코드에서는 3, 7 이 따로 치환된 것처럼 보이지만 실제로는 아래처럼 하나의 튜플이 대입된 것이다.
```python
(a,b) = (3, 7)        # tuple(a,b) = tuple(3, 7)
print(a,b)
```

>*다중 치환을 이용한 파이썬의 Swap()*
```
a, b = b, a
print(a,b)
```

#### 산술 연산
```
print(a + b)
print(a - b)
print(a * b)
print(a / b)        # 실수 나눗셈
print(a ** b)       # 지수 연산
print(a // b)       # 정수 나눗셈(몫)
print(a % b)        # 나머지
```

#### 문자 핸들링
```python
print('hello' + 'python')           # hellopython
print('hello' * 3)
```
#### 관계 연산자
```
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)
```
#### python 의 범위 연산자
아래와 같은 범위 연산 표현은 파이썬의 주요한 특징이다.
```python
age = 15
print(10 <= age <= 19)          # True
```
#### 논리 연산
AND / OR 연산이 가능핟.
```python
print(True and True)            # True
print(True and False)           # False
print(False and True)           # False
print(False and False)          # False
```
#### if 문
파이썬의 조건문은 if~else / elif 로 사용한다. switch 문은 존재하지 않는다.
```python
a = 3
if a % 2 == 1:
    print('홀수')
else:
    print('짝수')

if a < 0:
    print('음수')
elif a > 0:
    print('양수')
else:
    print('제로')
```

#### 함수
python 의 함수는 def 를 사용하여 선언한다. 기본적으로 python의 함수는 return 을 명시하지 않아도 기본적으로 'None'를 반환한다.
```python
def f_1(c, d):
    print('f_1', c+d)
    return c+d
print(f_1(12, 34))          # return 을 명시하지 않아도 기본 반환값 None을 호출한다.
```

#### 반복문
for 문을 이용하여 반복문을 수행한다. range() 함수를 이용하면 쉽게 반복이 가능하다. 아래는 range() 를 이용한 여러 가지 방식이다.
```python
for i in range(5):                  # 0~4까지 반복
    print(i, end=' ')

for i in range(0,5):                # 0~4까지 반복
    print(i, end=' ')

for i in range(0, 5, 1):            # 0~4까지 1씩 반복, 2라면, 0 ,2, 4로 세 번 반복
    print(i, end=' ')

for i in reversed(range(5)):        # python reversed 4 ~ 0 까지 반복.
    print(i, end=' ')

for i in enumerate(range(5,10)):    # enumerate : 나열하다. # 자신만의 인덱스를 사용. 5 ~ 9까지 반복 
    print(i, end=' ')
# (결과) (0, 5) (1, 6) (2, 7) (3, 8) (4, 9)
```

#### Collections : list, tuple, set, dictionary
#### list 
```python
a = [1, 3, 5]                    
print(a)                        # [1, 3, 5]
print(a[0], a[1], a[2])         # 1 3 5

for i in range(len(a)):         # len(a)=3 반복
    print(i, a[i])

for i in a:                     # a 3번 반복
    print(i, end= ' ')
```
list 에는 여러 가지 형태를 넣을 수 있다.
```python
c = [2,4,6]
c.append(8)                     # [2, 4, 6, 8]
c.append([10])                  # [2, 4, 6, 8, 10]

c.extend(12)                    # error. 12 라는 숫자 타입(int) 을 extend 할 수 없다.
c.extend([14])                  # extend 함수는 같은 list 간에 확장시 이용. 반드시 list 로 넣어줘야한다.

c+= 16                          # error
c += [16]                       # extend 함수와 + 연산자는 동일한 효과를 가진다. 반드시 list로 + 해야 한다.

c[0] = 99
print(c)                        # [99, 4, 6, 8, 10]
```

#### tuple
list와 동일하게 사용할 수 있다. [] 는 list, () 는 tuple. 하지만 변경할 수 없으므로, '상수 리스트' 라고도 부른다.
```python
d = (1, 3, 5)
print(d)                        # (1, 3, 5)

for i in d:
    print(i)                    # 1 3 5

d[0] = 1                        # error. 튜플은 데이터를 변경할 수 없다.
d.append(17)                    # error.
```
tuple은 파이썬 내부 계산에서 많이 사용한다.다중 치환이 되는 이유도 tuple 때문임, 아래와 같이 다중 치환할 경우, 튜플 하나를 대입하는 것과 같다.
```python
(a1, a2) = (3, 4)
print(a1, a2)                   # 3 4

a3 = (1,2)
a4, a5 = a3                 
print(a4, a5)                   # 1 2

def f_2(a, b):
    return a-b, a+b             # 반환값이 여러 개인 경우, tuple 로 묶어서 하나 반환함.

print(f_2(7,3))                 # 반환값 (4,10)

a6, a7 = f_2(7,3)
print(a6, a7)                   # 4 10
```
#### dictionary
```python
d = {'name' : 'DONGGOO', 'age' : 20, 3 : 4}         # 3도 딕셔너리의 키 값으로 사용 가능.
print(d)                                            # {'age': 20, 3: 4, 'name': 'DONGGOO'}
print(d['name'], d['age'], d[3])                     # DONGGOO 20 4

# d2 = dict(name = 'hoon', age = 20, 3 = 4)           # Error. int형은 '=' 로 불가능.

d['addr'] = 'Seoul'                                 # 데이터 추가 가능.
print(d)                                            # {'age': 20, 3: 4, 'name': 'DONGGOO', 'addr': 'Seoul'}

for k in d :                                        # 반복문 가능.
    print(k, d[k])
```

#### argument
##### Positional & Keyword argument
```python
def f_3(a, b, c):
    print(a, b, c, sep='**', end='\n\n')            # sep=seperator, default 공백

f_3(1, 2, 3)                                        # positional argument
f_3(a=1, b=2, c=3)                                  # keyword argument
f_3(b=2, c=3, a=1)
f_3(1, b=2, c=3)                                    # positional 과 keyword 방식 섞어 사용할 수도 있다.
# f_3(a=1, 2 , c=3)                                   # error. position은 keyword 앞에 사용해야 함.
```
##### 가변 인자 전달 방식
```python
def f_4(*args):                                     # 가변 인자, 앞쪽에 *를 붙이면 된다. packing
    print(args, *args)                              # *, (force) unpacking

f_4()
f_4(1)
f_4(1,2)
f_4(1,2,3)
```
##### 키워드 가변 인자
```python
def f_5(**kwargs):                                  # keyword 가변 인자 # 반드시 keyword 형태로 전달해야 한다.
    print(kwargs)
    print(type(kwargs))                             # data 형태 dictionary

f_5()
f_5(a=1)
f_5(a=1, b=2)

# dictionary 를 만드는 함수. dict 함수와 동일
def f_6(**kwargs):
    return kwargs

d = f_6(a=1, b=2)
print(d)
```