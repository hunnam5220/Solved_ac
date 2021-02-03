from sys import stdin
from math import factorial as ft

while 1:
    arr = list(reversed(stdin.readline().rstrip()))
    result = 0
    fn = 1

    if len(arr) == 1 and int(arr[0]) == 0:
        break

    else:
        for x in arr:
            result += int(x) * ft(fn)
            fn += 1
    print(result)