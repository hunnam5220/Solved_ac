from sys import stdin, setrecursionlimit
setrecursionlimit(10**8)
n, m = map(int, stdin.readline().split())

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


for i in range(m):
    a, b = map(int, stdin.readline().split())
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    else:
        print(i + 1)
        exit()

print(0)