from sys import stdin
import sys
sys.setrecursionlimit(10000)


def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False


t = int(stdin.readline().rstrip())
for h in range(t):
    result = 0
    m, n, k = map(int, stdin.readline().rstrip().split())
    graph = []
    for step in range(m):
        graph.append([0] * n)

    for j in range(k):
        a, b = map(int, stdin.readline().rstrip().split())
        graph[a][b] = 1

    for x in range(m):
        for y in range(n):
            if dfs(x, y):
                result += 1

    print(result)