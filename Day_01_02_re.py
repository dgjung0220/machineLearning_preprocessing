# Day_01_02_re.py
import re  # regular expression
import requests
import json

def re_basic():
    db = '''3412    [Bob] 123
    3834  Jonny 333
    1248   Kate 634
    1423   Tony 567
    2567  Peter 435
    3567  Alice 535
    1548  Kerry 534'''
    # print(db)

    temp = re.findall(r'[0-9]', db)   # r : raw
    print(temp)

    numbers = re.findall(r'[0-9]{4}', db)  # 3자리 구분 불가
    print(numbers)                         # ['3412', '3834', '1248', '1423', '2567', '3567', '1548']

    numbers = re.findall(r'[0-9]+', db) # 한 개 이상의 숫자 찾음
    print(numbers)

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

# request 모듈의 사용
url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
received = requests.get(url)
print(received)
print(received.text)

# decoding
text = received.content.decode('utf-8')
print(text)

# 문제
# 코드 번호와 도시 이름만 깔끔하게 출력해주세요.
codes = re.findall(r'\d+', text)
print(codes)
#cities = re.findall(r'[^"[{A-Za-z0-9_]+', text)
cities = re.findall(r'[가-힣]+', text)
print(cities)
print('-'*50)

# 중요
# .+ : 탐욕적 (greedy)
# .+? : 비탐욕적 (non-greedy)
codes = re.findall(r'"code":"([0-9]+)"', text)
print(codes)
cities = re.findall(r'"value":"(.+?)"', text)
print(cities)
print('-' * 50)

# 문제
# 코드 번호와 도시 이름을 동시에 찾아 보세요.
# findall 함수를 1회만 사용합니다.
# result = re.findall(r'"code":"(.+?)"."value":"(.+?)"', text)
result = re.findall(r'.+?:"(.+?)"."value":"(.+?)"', text)
print(result)
# 다중 치환을 이용한 tuple print
for code, city in result:
    print(code, city)

# jsonString = json.loads(text)
# for i in jsonString:
#    print(i['code'], ':', i['value'])