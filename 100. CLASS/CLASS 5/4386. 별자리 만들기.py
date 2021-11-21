from sys import stdin

n = int(stdin.readline())
arr = [[int(1e9)] * n for _ in range(n)]
xy = []
res = 0
stars = []

for _ in range(n):
    x, y = map(float, stdin.readline().split())
    xy.append((x, y))

for i in range(n):
    x1, y1 = xy[i]
    for j in range(i + 1, n):
        x2, y2 = xy[j]
        dist = (abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5
        arr[i][j] = dist
        arr[j][i] = dist

        stars.append((dist, i, j))

stars.sort()
parent = [x for x in range(n)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a


for dist, i, j in stars:
    if find_parent(parent, i) != find_parent(parent, j):
        union_parent(parent, i, j)
        res += dist

print(round(res, 2))