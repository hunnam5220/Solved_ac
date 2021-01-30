from sys import stdin
from math import pi

n = 1
while True:
    r, cycle, time = map(float, stdin.readline().rstrip().split())

    if cycle == 0:
        break
    else:
        distance = '%.2f' % ((r * pi * cycle) / 63360)
        mph = '%.2f' % (((r * pi * cycle) / 63360) / time * 3600)
        print('Trip #{}: {} {}'.format(n, distance, mph))
        n += 1
