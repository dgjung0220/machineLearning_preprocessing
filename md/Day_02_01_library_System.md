### 공공 데이터 다루기 - 도서관 빈 자리 찾기
XML이나 JSON 으로 정돈되지 않은 웹사이트의 데이터 정보 또한 쉽게 다룰 수 있다. [성남시 중앙 도서관](http://ct.snlib.go.kr/snct/03_study/56_dataroom.asp) 에는
실시간 좌석 현황을 제공하는데 이 데이터 내용을 파싱하여 빈 자리의 갯수 및 위치를 알아내자. [소스코드](../Day_02_01_library.py)

```python
url = 'http://211.253.111.151:8089/EZ5500/SEAT/RoomStatus.aspx'
received = requests.get(url)
print(received)

text = received.content.decode('euc-kr')

seats_style = re.findall(r'<td class=(.+?) style="text-align: center;width:30px;height:25px; font-size:10px;">', text)
all_seats = re.findall(r'([0-9]+)</td>', text)

seats_style = np.array(seats_style)
all_seats = np.array(all_seats)
empty_seats = all_seats[seats_style == "'Style1'"]

print('Count of remained seats : ', len(empty_seats))
print(*empty_seats)
```

분당 중앙 도서관의 경우 re.DOTALL 로 한 번에 읽으면 이상하게 좌석이 잘 카운트되지 않은 문제가 있다. 그래서 전체 좌석을 읽어온 후, 빈 좌석을 다시 파싱했다.