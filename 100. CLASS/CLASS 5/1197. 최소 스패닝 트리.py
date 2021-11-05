from sys import stdin

n, m = map(int, stdin.readline().split())
parent = [x for x in range(n + 1)]
roads = []
for step in range(m):
    a, b, c = map(int, stdin.readline().split())
    roads.append((c, a, b))

roads.sort()


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


res = 0
for c, a, b in roads:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += c

print(res)