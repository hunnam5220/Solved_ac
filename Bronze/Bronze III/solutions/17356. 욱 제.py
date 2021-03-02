from sys import stdin

a, b = map(int, stdin.readline().split())

m = (b - a) / 400
print(1 / (1 + 10 ** m))