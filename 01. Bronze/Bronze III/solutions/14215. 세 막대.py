from sys import stdin
from collections import Counter as cc

a, b, c = sorted(list(map(int, stdin.readline().rstrip().split())))

chk = list(cc([a, b, c]).values())

if a == b == c:
    print(sum([a, b, c]))

elif 2 in chk:
    if a + b <= c:
        c = a + b - 1

    print(a + b + c)

else:
    if (a + b) <= c:
        c = a + b - 1

    if (c - b) > a:
        m = c - b - a
        c -= (m + 1)

    if (c - a) > b:
        m = c - a - b
        c -= (m + 1)

    print(a + b + c)