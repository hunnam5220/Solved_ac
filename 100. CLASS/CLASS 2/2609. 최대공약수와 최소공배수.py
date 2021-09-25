from sys import stdin
from math import gcd

a, b = map(int, stdin.readline().split())
g = gcd(a, b)
print(g)
print(a * b // g)