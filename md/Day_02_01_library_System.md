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
print('Seats : ', *empty_seats)
```

분당 중앙 도서관의 경우 re.DOTALL 로 한 번에 읽으면 이상하게 좌석이 잘 카운트되지 않은 문제가 있다. 그래서 전체 좌석을 읽어온 후, 빈 좌석을 다시 파싱했다.   

결과 :
```
Count of remained seats :  149
Seats : 2 3 4 6 7 9 10 11 12 24 23 22 20 19 18 17 16 13 27 28 29 30 31 33 34 35 48 47 46 44 41 40 38 37 49 50 51 52 53 54 55 56 57 58 59 71 70 69 67 66 64 63 62 61 73 74 75 76 80 81 82 83 84 95 92 91 89 87 86 97 98 99
100 101 102 103 104 105 107 119 118 117 116 113 112 111 110 122 123 124 125 126 127 128 129 131 132 144 142 140 139 137 135 134 146 148 149 152 153 154 155 168 167 166 165 164 163 160 158 157 170 172 173 175 176 177 178 179 190 189 187 185 183 181 194 195 196 198 204 203 201 206 207 208 209 210 215 213 212
```