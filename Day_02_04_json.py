# Day_02_04_json.py

import json
import requests

def not_used():
    j1 = '{"ip": "8.8.8.8"}'
    print(j1)

    j2 = json.loads(j1)
    print(j2)
    print(type(j2))

    j3 = json.dumps(j2)
    print(j3)
    print(type(j3))
    print('-'*50)

    valid = '''{
       "object_or_array": "object",
       "empty": false,
       "parse_time_nanoseconds": 19608,
       "validate": true,
       "size": 1
    }'''

    # 문제
    # valid 문자열에 포함된 값만 출력
    temp = json.loads(valid)
    for i in temp:
        print(temp[i])

def not_used2() :
    url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
    received = requests.get(url)
    text = received.content.decode('utf-8') # decoding

    # 문제
    # 코드 번호와 도시 이름을 json 모듈을 사용해서 출력해 보세요.
    jsonString = json.loads(text)
    for i in jsonString:
        print(i['code'], ':', i['value'])

url ='http://place.map.daum.net/main/v/SES3403?_=1513056646739'
received = requests.get(url)
print(received)
print(received.text)
# 문제
# 상행선 시간표만 출력해보세요.