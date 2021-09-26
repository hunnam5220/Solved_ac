from sys import stdin

xy = []

for _ in range(int(stdin.readline())):
    x, y = map(int, stdin.readline().split())
    xy.append((x, y))

xy.sort(key=lambda x: (x[1], x[0]))
for i in xy:
    print(*i)