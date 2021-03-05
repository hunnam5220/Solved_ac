from sys import stdin
import math

n = int(stdin.readline().rstrip())
scl = math.sqrt(3) * n

print(scl / 4 * math.sqrt(4*pow(n, 2) - pow(scl, 2)))