### Python 기본 문법
machine learning을 위한 tensorflow, scikit-learn 등을 다루기 위해 파이썬 기본 문법을 파악해야한다.

---
* 파이썬 관련 도서
    * (기본)[Try! helloworld 파이썬](http://www.yes24.com/24/Goods/35907623?Acode=101) 
    * (실력)[파이썬 코딩의 기술](http://www.yes24.com/24/goods/25138160?scode=032&OzSrank=1)
    * (분석-NumPy,pandas)[파이썬 라이브러리를 활용한 데이터 분석](http://www.hanbit.co.kr/store/books/look.php?p_code=B6540908288)
    * (분석-Scikitlearn)[파이썬 라이브러리를 활용한 머신러닝](http://www.hanbit.co.kr/store/books/look.php?p_code=B6119391002)
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
```
a,b = 3, 7
print(a,b)
```
위의 코드에서는 3, 7 이 따로 치환된 것처럼 보이지만 실제로는 아래처럼 하나의 튜플이 대입된 것이다.
```
(a,b) = (3, 7)        # tuple(a,b) = tuple(3, 7)
print(a,b)
```

>*다중 치환을 이용한 파이썬의 Swap()*
```
a, b = b, a
print(a,b)
```

