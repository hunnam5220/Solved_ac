from sys import stdin
from collections import Counter as cc

step = int(stdin.readline().rstrip())
p = 0

for s in range(step):
    arr = list(map(int, stdin.readline().rstrip().split()))
    chk = cc(arr)

    if 3 in chk.values():
        num = list(chk.items())[0][0]
        tmp = 10000 + num * 1000

    elif 2 in chk.values():
        num = max(chk.items(), key=lambda x: x[1])[0]
        tmp = 1000 + num * 100

    else:
        tmp = max(arr) * 100

    if p < tmp:
        p = tmp

print(p)