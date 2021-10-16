from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
arr = [x for x in range(1, n + 1)]
res = []
for i in list(set(combinations(arr, m))):
    res.append(i)

res.sort()
for i in res:
    print(*i)