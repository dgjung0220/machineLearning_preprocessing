# Day_01_01_python.py

# ctrl + shift + F10 / alt + shift + F10 : Run program

print(12, 3.14, True, 'hello')

# python의 네 가지 변수 타입 => <class 'int'> <class 'float'> <class 'bool'> <class 'str'>
print(type(12), type(3.14), type(True), type('hello'))

a = '123'
print(a, type(a))

# 문자열 a '123' 을 정수형으로 변환
a = int(a)
print(type(a))

# python 의 다중 치환
a,b = 3, 7
print(a,b)

# pytho 의 swap
a, b = b, a
print(a,b)

# 산술 연산
print(a + b)
print(a - b)
print(a * b)
print(a / b)   # 실수 나눗셈
print(a ** b)  # 지수 연산
print(a // b)  # 정수 나눗셈(몫)
print(a % b)   # 나머지
print('-' * 50)

# 문자 핸들링
print('hello' + 'python')
print('hello' * 3)
print('-' * 50)

# 관계 연산자
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)
print('-' * 50)

# python의 범위 연산자
age = 15
print(10 <= age <= 19)
print('-' * 50)

# 논리 연산
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print('-' * 50)

# 제어문
# if 문
a = 3
if a % 2 == 1:
    print('홀수')
else:
    print('짝수')

# if elif
if a < 0:
    print('음수')
elif a > 0:
    print('양수')
else:
    print('제로')
# python 에는 switch 문은 존재하지 않는다.
print('-' * 50)

# 함수
def f_1(c, d):
    print('f_1', c+d)
    return c+d

print(f_1(12, 34)) # return 을 명시하지 않아도 기본 반환값 None을 호출한다.
print('-' * 50)

# 아래의 range 함수 모두 동일함.
for i in range(5):
    print(i, end=' ')
print()

for i in range(0,5):
    print(i, end=' ')
print()

for i in range(0, 5, 1):
    print(i, end=' ')
print()

# python reversed 4 ~ 0 까지 반복.
for i in reversed(range(5)):
    print(i, end=' ')
print()

# enumerate : 나열하다.
# 자신만의 index를 사용. 0부터.
for i in enumerate(range(5,10)):
    print(i, end=' ')
print()
print('-' * 50)

# collections : list, tuple, set, dictionary
a = [1, 3, 5]
print(a)
print(a[0], a[1], a[2])

for i in range(len(a)):
    print(i, a[i])

for i in a:
    print(i, end= ' ')
print()
print('-'*50)

# 문제
# b 를 거꾸로 뒤집어 보세요.
b = list(range(10))
print(b)

# 뒤집기 코드
c = []
for i in reversed(b):
    c.append(i)
b = c
print(b)
print('-' * 50)

# list는 여러가지 데이터 형태를 넣을 수 있다.
c = [2,4,6]
c.append(8)
c.append([10])
# c.extend(12) # error
c.extend([14]) # extend 함수는 같은 list 간에 확장시 이용. 반드시 list 로 넣어줘야한다.
# c+= 16       # error
c += [16]      # extend 함수와 + 연산자는 동일한 효과를 가진다. 반드시 list로 + 해야 한다.
c[0] = 99
print(c)
print('-' * 50)

# tuple - list와 동일하게 사용할 수 있다. [] 는 list, () 는 tuple
# 변경할 수 없으므로, '상수 리스트' 라고도 부른다.
d = (1, 3, 5)
print(d)

for i in d:
    print(i)

# error 튜플은 데이터를 변경할 수 없다.
# d[0] = 1
# d.append(17)
print('-'* 50)

# tuple은 파이썬 내부 계산에서 많이 사용한다.
# 다중 치환이 되는 이유도 tuple 때문임, 아래와 같이 다중 치환할 경우, 튜플 하나를 대입하는 것과 같음.
(a1, a2) = (3, 4)
print(a1, a2)
a3 = (1,2)
a4, a5 = a3
print(a4, a5)

def f_2(a, b):
    return a-b, a+b
# 반환값이 여러 개인 경우, tuple 로 묶어서 하나 반환함.
print(f_2(7,3))   # 반환값 (4,10)

a6, a7 = f_2(7,3)
print(a6, a7) # 4 10

# dictionary, 함수 확장
a6, a7 = f_2(7, 3)
print(a6, a7)
print('-' * 50)

# 영한 사전 : 영어 단어를 찾으면 한글 설명이 나옴.
# 영어 단어 : key
# 한글 설명 : value

#     key             value
d = {'name' : 'hoon', 'age' : 20, 3 : 4}
print(d)
print(d['name'], d['age'])

d2 = dict(name = 'hoon', age = 20)
# d2 = dict(name = 'hoon', age = 20, 3 = 4) # 에러
print(d2)

# 데이터 추가시, 아래와 같이 정의
d2['addr'] = 'suji'
print(d2)

# 반복문도 가능.
for k in d2 :
    print(k, d2[k])
print('-' * 50)

def f_3(a, b, c):
    print(a, b, c, sep='**', end='\n\n') # sep의 default는 공백

f_3(1, 2, 3)                # positional argument
f_3(a=1, b=2, c=3)          # keyword argument
f_3(b=2, c=3, a=1)
f_3(1, b=2, c=3)            # positional 과 keyword 방식 섞어 사용할 수도 있다.
# f_3(a=1, 2 , c=3)         # position은 keyword 앞에 사용해야 함. error
print('-'*50)

def f_4(*args):             # 가변 인자, 앞쪽에 *를 붙이면 된다. packing
    print(args, *args)      # (force) unpacking

f_4()
f_4(1)
f_4(1,2)
f_4(1,2,3)

# python 에서 * 가 사용되는 곳.
# a * b
# a *= b

a = [1, 3, 5]
print(a)                # [1, 3, 5] 한개 넘어감
print(*a)               # 1 3 5    force unpacking, 세 개 넘어가는 효과
print(*a, sep='\n')     # 반복문 print 처럼사용 가능
print('-' * 50)

def f_5(**kwargs):          # keyword 가변 인자 # 반드시 keyword 형태로 전달해야 한다.
    print(kwargs)
    print(type(kwargs))     # data 형태 dictionary

# 문제
# f_5 를 호출하는 3 가지 방법
f_5()
f_5(a=1)
f_5(a=1, b=2)

# dictionary 를 만드는 함수. dict 함수와 동일
def f_6(**kwargs):
    return kwargs

d = f_6(a=1, b=2)
print(d)


