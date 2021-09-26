from sys import stdin
import statistics
from collections import Counter

arr = []
n = int(stdin.readline())
for _ in range(n):
    arr.append(int(stdin.readline()))

arr.sort()
print(round(sum(arr) / n))
print(statistics.median(arr))

cnt = set()
temp = 0
for a, b in list(Counter(arr).most_common()):
    if temp == 0:
        temp = (a, b)
        cnt.add((a, b))

    if temp[1] == b:
        cnt.add((a, b))

cnt = sorted(list(cnt))
print(cnt[0][0] if len(cnt) == 1 else cnt[1][0])
print(max(arr) - min(arr))