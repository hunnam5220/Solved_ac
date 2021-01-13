from sys import stdin
import datetime

h_m = stdin.readline().rstrip()
second = int(stdin.readline().rstrip())

time = datetime.datetime.strptime(h_m, '%H %M %S') + datetime.timedelta(seconds=second)

print(time.hour, time.minute, time.second)