from sys import stdin
import datetime

t1, t2 = 0, 0

for c in range(2):
    data = stdin.readline().rstrip().split(':')
    for i in range(len(data)):
        if i == 0:
            t1 += int(data[i]) * 3600
        elif i == 1:
            t1 += int(data[i]) * 60
        else:
            t1 += int(data[i])

    if c == 0:
        t2 = t1
        t1 = 0
    else:
        if t1 < t2:
            print(t1 - t2 + 3600 * 24)
        else:
            print(t1 - t2)