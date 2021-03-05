from sys import stdin
from collections import Counter as cc

n = int(stdin.readline().rstrip())

arr = list(map(int, stdin.readline().rstrip().split()))
print(cc(arr)[n])
