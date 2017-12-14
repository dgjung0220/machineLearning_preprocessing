# Day_04_08_weather_re.py

import requests
import re

# 서울시 기본 정보 사이트에서
# 평균 기온, 최고기온, 최저 기온 데이터를 파싱
# http://www.kma.go.kr/weather/climate/past_cal.jsp
url = 'http://www.kma.go.kr/weather/climate/past_cal.jsp'
received = requests.get(url)

# table = re.findall(r'<tbody>(.+?)</tbody>', received.text, re.DOTALL)
# results = re.findall(r'<td class="align_left">(.+?)<br />(.+?)<br />(.+?)<br />', table[0])
# for i, result in enumerate(results, 1):
#     print('{:2} : {}, {}, {}'.format(i, *result))

tbody = re.findall(r'<tbody>(.+?)</tbody>', received.text, re.DOTALL)
trs = re.findall(r'<tr>(.+?)</tr>', tbody[0], re.DOTALL)
# print(len(trs))

days = []
for tr in trs[1::2]:
    # print(tr)
    tds = re.findall(r'<td class="align_left">(.+?)</td>', tr)
    tds = [i for i in tds if not '&nbsp;' in i]

    # print(tds)
    days += tds

for day in days:
    # print(day)

    items = re.findall(r':(.+?)℃', day)
    print(items)