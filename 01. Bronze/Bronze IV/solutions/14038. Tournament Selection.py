from sys import stdin
from collections import Counter as cc

arr = []
for x in range(6):
    arr.append(stdin.readline().rstrip())

wins = cc(arr)['W']

if wins == 0:
    print(-1)
elif wins <= 2:
    print(3)
elif 2 < wins <= 4:
    print(2)
else:
    print(1)