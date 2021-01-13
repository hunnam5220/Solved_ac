from sys import stdin
from collections import Counter as cc

days = int(stdin.readline().rstrip())
cars = list(map(int, stdin.readline().rstrip().split()))

print(cc(cars)[days])