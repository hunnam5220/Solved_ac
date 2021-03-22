from sys import stdin


def find_parent(parent, x):
    if parent[x - 1] != x:
        parent[x - 1] = find_parent(parent, parent[x - 1])
    return parent[x - 1]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b - 1] = a
    else:
        parent[a - 1] = b


e, v = map(int, stdin.readline().split())
parent = [_ for _ in range(1, e + 1)]
edges = []

for _ in range(v):
    a, b, c = map(int, stdin.readline().split())
    edges.append((c, a, b))

edges.sort()

result = 0
last = 0

for x in edges:
    cost, a, b = x

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)
"""
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""