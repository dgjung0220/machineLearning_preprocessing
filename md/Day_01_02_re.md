### Regular Expression

머신러닝에 필요한 데이터를 수집, 정제하기 위해서 RE(정규 표현식)을 많이 이용한다. 정규 표현식의 역사, 기본 개념, 문법은 한글 위키피디아에 잘 정리되어 있다.
>정규 표현식(正規表現式, 영어: regular expression, 간단히 regexp 또는 regex, rational expression) 또는 정규식(正規式)은 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식 언어이다. 정규 표현식은 많은 텍스트 편집기와 프로그래밍 언어에서 문자열의 검색과 치환을 위해 지원하고 있으며, 특히 펄과 Tcl은 언어 자체에 강력한 정규 표현식을 구현하고 있다.-[위키피디아](https://ko.wikipedia.org/wiki/%EC%A0%95%EA%B7%9C_%ED%91%9C%ED%98%84%EC%8B%9D)

### Re in Python
파이썬에서 정규표현식을 이용하기 위해서 Re 모듈을 이용한다. `import re`  
아래와 같은 db 파일에서 정규 표현식을 이용하여 정보를 뽑아보자.
```
db = '''
    3412    [Bob] 123
    3834  Jonny 333
    1248   Kate 634
    1423   Tony 567
    2567  Peter 435
    3567  Alice 535
    1548  Kerry 534'''
```

####숫자 찾기  
파이썬의 정규 표현식을 사용하는 문법은 `re.findall(r'', db)`를 사용한다. r 은 raw를 가리킨다.
위의 db에서 숫자 하나를 뽑는 방법은 아래와 같다. 
```
temp = re.findall(r'[0-9]', db)             # r : raw
print(temp)

# ['3', '4', '1', '2', '1', '2', '3', '3', '8', '3', '4', '3', '3', '3', '1', '2', '4', '8', '6', '3', '4', '1', '4', '2', '3', '5', '6', '7', '2', '5', '6', '7', '4', '3', '5', '3', '5', '6', '7', '5', '3', '5', '1', '5', '4', '8', '5', '3', '4']
```

####4자리 숫자  
한 자리가 아닌 여러 자리의 경우 {자릿 수}를 사용한다.
```
numbers = re.findall(r'[0-9]{4}', db)       # 3자리 구분 불가
print(numbers)                              

# ['3412', '3834', '1248', '1423', '2567', '3567', '1548']
```

####여러 자리 수 판별
db에 있는 세 자리 / 네 자리의 모든 숫자를 구분하기 위해서 + 기호를 사용한다. 덧셈 기호는 1번 이상의 발생을 의미한다. 이를테면 ab+c는 "abc", "abbc", "abbbc" 등을 일치시키지만 "ac"는 일치시키지 않는다.
```
numbers = re.findall(r'[0-9]+', db)         # 한 개 이상의 숫자 찾음
print(numbers)

# ['3412', '123', '3834', '333', '1248', '634', '1423', '567', '2567', '435', '3567', '535', '1548', '534']
```

```
# 문제
# 이름만 찾아 보세요.
name = re.findall(r'[A-Z][a-z]+', db)
print(name)

# T로 시작하는 이름만 찾아보세요.
name_t = re.findall(r'T[a-z]+', db)
print(name_t)

# T로 시작하지 않는 이름
name_not_t = re.findall(r'[A-SU-Z][a-z]+', db)
print(name_not_t)
```