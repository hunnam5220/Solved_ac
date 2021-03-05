from sys import stdin

a, b = map(int, stdin.readline().rstrip().split())
arr = []
for x in range(-1000, 1000, 1):
    if x ** 2 + 2 * a * x + b == 0:
        arr.append(x)

print(' '.join(map(str, arr)))