from sys import stdin
x, y, n = map(int, stdin.readline().rstrip().split())

if (y - x) % n != 0:
    cnt = 1
else:
    cnt = 0

print((y - x) // n + cnt)