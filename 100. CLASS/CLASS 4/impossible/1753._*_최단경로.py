from sys import stdin

INF = int(1e9)
v, e = map(int, stdin.readline().split())
root = int(stdin.readline())
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, v + 1):
    if i == root:
        print(0)
    else:
        print(graph[root][i]) if graph[root][i] != INF else print('INF')
