from sys import stdin
from collections import Counter as cc

arr = []
for x in range(3):
    arr.append(int(stdin.readline().rstrip()))

if sum(arr) != 180:
    print('Error')

elif arr[0] == arr[1] == arr[2] == 60:
    print('Equilateral')

elif (sum(arr) == 180) and (sorted(list(cc(arr).values()))[1] == 2):
    print('Isosceles')

elif (sum(arr) == 180) and (sorted(list(cc(arr).values()))[1] == 1):
    print('Scalene')