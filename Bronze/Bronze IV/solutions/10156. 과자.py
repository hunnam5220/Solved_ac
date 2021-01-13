from sys import stdin

p, n, m = map(int, stdin.readline().rstrip().split())


if p * n >= m:
    print(p * n - m)
else:
    print(0)