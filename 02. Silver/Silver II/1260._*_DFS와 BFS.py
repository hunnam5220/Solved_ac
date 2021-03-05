from collections import deque
from sys import stdin

n, m, v = map(int, stdin.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]

for step in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for step in graph:
    step.sort()


def dfs(graph, visited, v):
    visited[v - 1] = True
    print(v, end=' ')
    for step in graph[v]:
        if not visited[step - 1]:
            dfs(graph, visited, step)


def bfs(graph, visited, v):
    q = deque([v])
    visited[v-1] = True

    while q:
        k = q.popleft()
        print(k, end=' ')

        for step in graph[k]:
            if not visited[step - 1]:
                q.append(step)
                visited[step - 1] = True


arr = [False] * n
dfs(graph, arr, v)
print()
visited = [False] * n
bfs(graph, visited, v)