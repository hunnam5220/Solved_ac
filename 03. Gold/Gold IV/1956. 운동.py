from sys import stdin

inf = int(1e9)
n, m = map(int, stdin.readline().split())
graph = [[inf] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a][b] = c


for k in range(1, n + 1):
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])


ans = inf
for i in range(1, n + 1):
    ans = min(graph[i][i], ans)

print(-1 if ans == inf else ans)