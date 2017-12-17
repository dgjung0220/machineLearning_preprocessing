# Day_02_01_library.py

import re
import requests
import numpy as np

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

# 용인 수지 도서관 좌석 현황
def suji_library():
    url = 'http://211.251.214.169:8080/SeatMate_sj/SeatMate.php?classInfo=5'
    received = requests.get(url)
    print(received)
    #print(received.text)

    text = received.content.decode('euc-kr')
    #empty_seats = re.findall(r'>(\d+)</div>', text, re.DOTALL);
    empty_seats = re.findall(r'>([0-9]+?)</div>', text, re.DOTALL);

    print(empty_seats)