from sys import stdin
import math

n, k = map(int, stdin.readline().rstrip().split())
arr = list(map(int, stdin.readline().rstrip().split()))
cnt = 0

for step in arr:
    cnt += math.ceil(step / 2)

if n > cnt:
    print('NO')
else:
    print('YES')