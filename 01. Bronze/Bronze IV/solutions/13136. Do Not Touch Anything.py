from sys import stdin

r, c, n = map(int, stdin.readline().rstrip().split())

if r % n != 0:
    r += (n - (r % n))

if c % n != 0:
    c += (n - (c % n))

print(int((r * c) / n ** 2))