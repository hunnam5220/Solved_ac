from sys import stdin

a = stdin.readline().rstrip().split(':')
b = stdin.readline().rstrip().split(':')

s1 = 3600 * int(a[0]) + 60 * int(a[1]) + int(a[2])
s2 = 3600 * int(b[0]) + 60 * int(b[1]) + int(b[2])

data = s2 - s1

hour = data // 3600
if hour < 0:
    hour = 24 + hour

data %= 3600
minute = data // 60

data %= 60

print('%.2d:%.2d:%.2d' % (hour, minute, data))