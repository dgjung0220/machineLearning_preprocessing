### JSON

>JSON (JavaScript Object Notation)은 경량의 DATA-교환 형식이다. 이 형식은 사람이 읽고 쓰기에 용이하며, 기계가 분석하고 생성함에도 용이하다. JavaScript Programming Language, Standard ECMA-262 3rd Edition - December 1999의 일부에 토대를 두고 있다. JSON은 완벽하게 언어로 부터 독립적이지만 C-family 언어 - C, C++, C#, Java, JavaScript, Perl, Python 그외 다수 - 의 프로그래머들에게 친숙한 관습을 사용하는 텍스트 형식이다. 이러한 속성들이 JSON을 이상적인 DATA-교환 언어로 만들고 있다.-[JSON.ORG](https://www.json.org/json-ko.html)


### 개요

python에서는 JSON 관련 함수로 loads() 와 dumps()를 제공한다. JSON 문자열을 Python 타입(Dict, List, Tuple) 등으로 변경하는 것을 JSON Decoding이라 하고 json.loads() 함수를 사용한다. 반대로 Python Object 를 JSON 문자열로 변환하는 것을 JSPN Encoding이라고 하며, json.dumps() 를 사용한다.

```python
j1 = '{"ip": "8.8.8.8"}'
print(j1)                   # {"ip": "8.8.8.8"}

j2 = json.loads(j1)
print(j2)                   # {"ip": "8.8.8.8"}
print(type(j2))             # <class 'dict'>

j3 = json.dumps(j2)
print(j3)                   # {"ip": "8.8.8.8"}
print(type(j3))             # <class 'dict'>
```

```python
valid = '''{
    "object_or_array": "object",
    "empty": false,
    "parse_time_nanoseconds": 19608,
    "validate": true,
    "size": 1
}'''

# valid 문자열에 포함된 값만 출력
temp = json.loads(valid)
for i in temp:
    print(temp[i])                          # object\nFalse\n19068\nTrue\n1
```

### Requests 모듈을 이용하여 외부 JSON 정보 이용하기
```python
url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
received = requests.get(url)

text = received.content.decode('utf-8')     # 문자decoding

jsonString = json.loads(text)
    for i in jsonString:
        print(i['code'], ':', i['value'])
```