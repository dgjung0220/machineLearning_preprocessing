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

print()