from sys import stdin
from itertools import permutations
from math import gcd

for _ in range(int(stdin.readline())):
    arr = list(map(int, stdin.readline().split()))
    ans = 0
    for x, y in list(set(permutations(arr, 2))):
        ans = max(ans, gcd(x, y))
    print(ans)