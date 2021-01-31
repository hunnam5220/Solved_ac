from sys import stdin
from datetime import datetime as dt

a = dt.strptime(stdin.readline().rstrip(), '%H:%M:%S')
b = dt.strptime(stdin.readline().rstrip(), '%H:%M:%S')
utc = dt.strptime('00:00:00', '%H:%M:%S')


result = dt.strftime(utc - (a - b), '%H:%M:%S')

if result == '00:00:00':
    print('24:00:00')
else:
    print(result)