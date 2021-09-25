from sys import stdin
import math
a, b = map(int, stdin.readline().split())

x = math.factorial(a)
y = (math.factorial(b) * math.factorial(a-b))
res = x // y
print(res)