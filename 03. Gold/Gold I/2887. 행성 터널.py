from sys import stdin


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


n = int(stdin.readline().rstrip())
parent = [0] * (n + 1)
for i in range(1, n):
    parent[i] = i

result = 0
xs = []
ys = []
zs = []
datas = []

for i in range(n):
    x, y, z = map(int, stdin.readline().split())
    xs.append((x, i))
    ys.append((y, i))
    zs.append((z, i))

xs.sort()
ys.sort()
zs.sort()

for i in range(n - 1):
    datas.append((xs[i + 1][0] - xs[i][0], xs[i][1], xs[i + 1][1]))
    datas.append((ys[i + 1][0] - ys[i][0], ys[i][1], ys[i + 1][1]))
    datas.append((zs[i + 1][0] - zs[i][0], zs[i][1], zs[i + 1][1]))

datas.sort()

for data in datas:
    cost, x, y = data

    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(result)
