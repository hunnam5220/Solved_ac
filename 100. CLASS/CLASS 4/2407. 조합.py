from sys import stdin
import math
n, m = map(int, stdin.readline().split())
print(int(math.factorial(n) // (math.factorial(abs(n - m)) * math.factorial(m))))