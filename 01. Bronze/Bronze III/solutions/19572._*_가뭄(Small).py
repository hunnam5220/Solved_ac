from sys import stdin

d1, d2, d3 = map(int, stdin.readline().rstrip().split())

if (d1 + d2 - d3) / 2 <= 0 or (d1 - d2 + d3) / 2 <= 0 or (-d1 + d2 + d3) / 2 <= 0:
    print(-1)
else:
    print(1)
    print(round((d1 + d2 - d3) / 2, 1), round((d1 - d2 + d3) / 2, 1), round((-d1 + d2 + d3) / 2, 1))