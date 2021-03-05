from sys import stdin
from collections import Counter as cc

while 1:
    arr = sorted(list(map(int, stdin.readline().rstrip().split())))

    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        break

    else:
        if arr[-1] >= sum(arr[:2]):
            print('Invalid')

        elif arr[0] == arr[1] == arr[2]:
            print('Equilateral')

        elif 2 in cc(arr).values():
            print('Isosceles')

        else:
            print('Scalene')