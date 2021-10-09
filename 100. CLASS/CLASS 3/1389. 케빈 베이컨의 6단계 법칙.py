from sys import stdin
from collections import deque

inf = int(1e9)
n, m = map(int, stdin.readline().split())
arr = [set() for x in range(n + 1)]
res = [0 for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, stdin.readline().split())
    arr[a].add(b)
    arr[b].add(a)


def bfs(x, j):
    visited = set()
    visited.add(x)
    q = deque()
    q.append((0, x))
    temp = int(1e9)
    
    while q:
        cost, now = q.popleft()
        if now == j:
            temp = min(temp, cost)

        for i in arr[now]:
            if i not in visited:
                q.append((cost + 1, i))
                visited.add(i)

    res[j] += temp


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j:
            bfs(i, j)

print(res.index(min(res[1:])))