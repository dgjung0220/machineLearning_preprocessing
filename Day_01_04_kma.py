# Day_01_04_kma.py

import re
import requests

import csv

f = open('Data/kma.csv', 'w', encoding='utf-8', newline='') # file open # newline 속성을 쓰지 않으면 csv 파일에 빈 줄 없이 생성.
writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_ALL)                          # csv 모듈 writer # delimiter는 기본적으로 ',' # csv 모듈은 quot 옵션 설정이 가능하다.

# --------------------------------------------------------------------------------- #
url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
received = requests.get(url)
print(received)
# print(received.text)

# temp = re.findall(r'<province>(.+)</province>', received.text)
# print(temp)
# print(len(temp))

# 문제
# location 영역을 찾아보세요.
locations = re.findall(r'<location wl_ver="3">(.+?)</location>', received.text, re.DOTALL) # re.DOTALL : 찾으려고 하는 것이 여러 줄에 걸쳐 있을 때. 개행문자를 무시하고 찾는다.
# locations = re.findall(r'<location wl_ver="3">([\s\S]+?)</location>', received.text)
print(len(locations))
# print(locations)

for loc in locations:
    # print(loc)
    # province 와 city를 찾아 보세요.
    # province = re.findall(r'<province>(.+?)</province>', loc)
    # city = re.findall(r'<city>(.+?)</city>', loc)
    #print(province[0])
    #print(city[0])

    prov_city = re.findall(r'<province>(.+?)</province>.+?<city>(.+?)</city>', loc, re.DOTALL)
    print(*prov_city)

    # # 문제 데이터를 찾아보세요.
    # data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)
    # # print(len(data))
    # for datum in data:
    #     # 문제 mode, tmEf, wf, tmn tmx, reliabilty
    #     mode = re.findall(r'<mode>(.+?)</mode>', datum)
    #     tmEf = re.findall(r'<tmEf>(.+?)</tmEf>', datum)
    #     wf = re.findall(r'<wf>(.+?)</wf>', datum)
    #     tmn = re.findall(r'<tmn>(.+?)</tmn>', datum)
    #     tmx = re.findall(r'<tmx>(.+?)</tmx>', datum)
    #     reliability = re.findall(r'<reliability>(.+?)</reliability>', datum)
    #
    #     #print('     ' + mode[0], tmEf[0], wf[0], tmn[0], tmx[0], reliability[0])
    #
    #     # 한 번에 여섯 개의 데이터를 모두 걸러낼 수 있다.
    #     items = re.findall(r'>(.+?)<', datum)
    #     # print(province[0], city[0], *temp, file=f, sep=',') # unpacking, csv 모듈 안 쓰는 방법
    #
    #     # csv 모듈을 사용.
    #     row = [province[0], city[0]]
    #     row += items
    #
    #     print(row)
    #     writer.writerow(row)
# ------------------------------------------------------------------------------- #
f.close()