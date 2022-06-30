from math import sqrt
from sys import stdin

a, b = map(int, stdin.readline().split())

print('%.6lf' % (float((a + b) - sqrt(a * a + b * b))))