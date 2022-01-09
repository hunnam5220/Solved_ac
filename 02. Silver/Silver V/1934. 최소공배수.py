from sys import stdin
from math import gcd


def lcm(a, b):
    v = gcd(a, b)
    if v == 0:
        return 0

    else:
        return abs(a * b // v)


for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    print(lcm(a, b))
