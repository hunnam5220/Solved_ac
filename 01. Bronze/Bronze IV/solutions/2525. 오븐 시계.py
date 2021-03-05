from sys import stdin
import datetime

h_m = stdin.readline().rstrip()
min = int(stdin.readline().rstrip())

time = datetime.datetime.strptime(h_m, '%H %M') + datetime.timedelta(minutes=min)

print(time.hour, time.minute)