from collections import Counter as cc
from sys import stdin
arr = list(map(int, stdin.readline().split()))

equal_nums = max(cc(arr).values())
item = list(cc(arr).items())
sort_arr = max(item, key=lambda x:x[1])[0]

if equal_nums == 1:
    print(max(arr) * 100)
elif equal_nums == 3:
    print(10000 + arr[0] * 1000)
else:
    print(1000 + sort_arr*100)