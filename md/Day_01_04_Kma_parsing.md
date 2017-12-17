### KMA(대한민국 기상청) 데이터 다루기

[소스 코드](../Day_01_04_kma.py)   
기상청에서 제공하는 RSS 및 데이터를 이용하여 날씨 데이터를 이용할 수 있다.
```python
url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
received = requests.get(url)
print(received)
```
위의 url을 통해 중기 예보 XML 데이터를 얻을 수 있는데 여기에서 location 및 각종 data를 정규 표현식을 통해 뽑을 수 있다.
```xml
<location wl_ver="3">
    <province>서울ㆍ인천ㆍ경기도</province>
    <city>서울</city>
    <data>
        <mode>A02</mode>
        <tmEf>2017-12-20 00:00</tmEf>
        <wf>구름많음</wf>
        <tmn>-8</tmn>
        <tmx>2</tmx>
        <reliability>보통</reliability>
    </data>
    <data>
        <mode>A02</mode>
        <tmEf>2017-12-20 12:00</tmEf>
        <wf>구름많음</wf>
        <tmn>-8</tmn>
        <tmx>2</tmx>
        <reliability>낮음</reliability>
    </data>
    ...
```

#### re.DOTALL
위의 XML 데이터를 살펴 보면 각 locations 가 있고, 그 위치에 해당하는 data들의 정보가 있다. 이를 동시에 뽑기 위해서느
먼저 locations 를 찾고, 각 location을 순회하면서 데이터를 찾아야 한다. 정규 표현식이 match 하는 방법은 최적화, 성능을 위해 한 줄씩 match 할 뿐 기본적으로 여러 줄을 match 할 수 없다.
우리가 찾으려고 하는 데이터 형식은 <location>~</location> 사이에 여러 줄로 걸쳐 기술되어 있다. 여러 줄을 match 시키는 방법은 ``re.findall`` 에서 re.DOTALL 이라는 옵션을 줌으로써 가능하다.   
``re.DOTALL: 찾으려고 하는 것이 여러 줄에 걸쳐 있을 때. 개행문자를 무시하고 찾는다.``
```python
locations = re.findall(r'<location wl_ver="3">(.+?)</location>', received.text, re.DOTALL) 
```
#### 기타 데이터 파싱
```python
for location in locations:
    prov_city = re.findall(r'<province>(.+?)</province>.+?<city>(.+?)</city>', location, re.DOTALL)
    province, city = prov_city[0][0], prov_city[0][1]
    
    data = re.findall(r'<data>(.+?)</data>', location, re.DOTALL)
    
    for datum in data :
        items = re.findall(r'>(.+?)<', datum)
        print(province, city, *items)
```
결과 :
```
서울ㆍ인천ㆍ경기도 서울 A02 2017-12-20 00:00 구름많음 -8 2 보통
서울ㆍ인천ㆍ경기도 서울 A02 2017-12-20 12:00 구름많음 -8 2 낮음
서울ㆍ인천ㆍ경기도 서울 A02 2017-12-21 00:00 구름많고 눈 -5 3 보통
서울ㆍ인천ㆍ경기도 서울 A02 2017-12-21 12:00 구름많음 -5 3 보통
서울ㆍ인천ㆍ경기도 서울 A02 2017-12-22 00:00 맑음 -3 4 보통
서울ㆍ인천ㆍ경기도 서울 A02 2017-12-22 12:00 맑음 -3 4 보통
서울ㆍ인천ㆍ경기도 서울 A02 2017-12-23 00:00 구름조금 -3 5 보통
서울ㆍ인천ㆍ경기도 서울 A02 2017-12-23 12:00 구름많고 비/눈 -3 5 보통
서울ㆍ인천ㆍ경기도 서울 A02 2017-12-24 00:00 구름많음 -3 3 낮음
서울ㆍ인천ㆍ경기도 서울 A02 2017-12-24 12:00 구름많음 -3 3 보통
서울ㆍ인천ㆍ경기도 서울 A01 2017-12-25 00:00 구름많음 -4 2 보통
서울ㆍ인천ㆍ경기도 서울 A01 2017-12-26 00:00 구름조금 -7 1 보통
서울ㆍ인천ㆍ경기도 서울 A01 2017-12-27 00:00 구름많음 -7 1 높음
서울ㆍ인천ㆍ경기도 인천 A02 2017-12-20 00:00 구름많음 -7 1 보통
서울ㆍ인천ㆍ경기도 인천 A02 2017-12-20 12:00 구름많음 -7 1 낮음
서울ㆍ인천ㆍ경기도 인천 A02 2017-12-21 00:00 구름많고 눈 -4 3 보통
서울ㆍ인천ㆍ경기도 인천 A02 2017-12-21 12:00 구름많음 -4 3 보통
서울ㆍ인천ㆍ경기도 인천 A02 2017-12-22 00:00 맑음 -3 4 보통
...
```

#### 결과를 파일에 저장
파싱된 데이터의 결과를 csv file로 저장할 수 있다. 이 때 파이썬의 print 를 사용하거나 csv 모듈을 사용할 수 있다.
#### 1.1. Print
``f = open('Data/kma.csv', 'w', encoding='utf-8', newline=None)`` 을 통해 파일을 오픈하는데 이 때 newline 옵션을 None으로 주면 빈 줄 없이 생성할 수 있다.
```python
import re
import requests

f = open('Data/kma.csv', 'w', encoding='utf-8', newline=None)

url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
received = requests.get(url)

locations = re.findall(r'<location wl_ver="3">(.+?)</location>', received.text, re.DOTALL) 

for location in locations:
    prov_city = re.findall(r'<province>(.+?)</province>.+?<city>(.+?)</city>', location, re.DOTALL)
    province, city = prov_city[0][0], prov_city[0][1]
    
    data = re.findall(r'<data>(.+?)</data>', location, re.DOTALL)
    
    for datum in data :
        items = re.findall(r'>(.+?)<', datum)
        print(province, city, *items)

        # file 에 저장
        print(province, city, *items, file=f, sep=',')              # sep: Seperator (구분자)

f.close()
```
#### 1.2. CSV 모듈
CSV 모듈을 이용하면 writer 옵션에 quoting을 부여함으로써 각 칼럼 데이터에 quot 처리를 할 수 있다.
```python
import re
import requests
import csv

f = open('Data/kma.csv', 'w', encoding='utf-8', newline=None)
writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)

url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
received = requests.get(url)

locations = re.findall(r'<location wl_ver="3">(.+?)</location>', received.text, re.DOTALL) 

for location in locations:
    prov_city = re.findall(r'<province>(.+?)</province>.+?<city>(.+?)</city>', location, re.DOTALL)
    province, city = prov_city[0][0], prov_city[0][1]
    
    data = re.findall(r'<data>(.+?)</data>', location, re.DOTALL)
    
    for datum in data :
        items = re.findall(r'>(.+?)<', datum)
        print(province, city, *items)

        # CSV 모듈 
        row = [province, city]
        row += items
        writer.writerow(row)

f.close()
```