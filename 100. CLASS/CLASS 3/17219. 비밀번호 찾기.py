from sys import stdin

n, m = map(int, stdin.readline().split())
d = {}
for _ in range(n):
    a, b = stdin.readline().split()
    d[a] = b

for _ in range(m):
    print(d[stdin.readline().rstrip()])