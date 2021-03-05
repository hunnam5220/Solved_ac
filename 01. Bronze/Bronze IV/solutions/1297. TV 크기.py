from sys import stdin
import math
d, h, w = map(float, stdin.readline().split())

k = math.sqrt(h**2 + w**2)
print(int(h * d / k), int(w * d / k))