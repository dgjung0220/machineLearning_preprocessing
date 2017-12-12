# Day_02_01_library.py

import re
import requests

url = 'http://211.251.214.169:8080/SeatMate_sj/SeatMate.php?classInfo=5'
received = requests.get(url)
print(received)
#print(received.text)

text = received.content.decode('euc-kr')
#empty_seats = re.findall(r'>(\d+)</div>', text, re.DOTALL);
empty_seats = re.findall(r'>([0-9]+?)</div>', text, re.DOTALL);

print(empty_seats)