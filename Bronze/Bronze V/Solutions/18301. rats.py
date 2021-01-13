from sys import stdin
import math
n1, n2, n12 = map(int, stdin.readline().split())

print(math.floor((n1+1) * (n2+1) / (n12+1) - 1))