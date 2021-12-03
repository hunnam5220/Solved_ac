from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 8)

n = int(stdin.readline())
nodes = [[] for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)


