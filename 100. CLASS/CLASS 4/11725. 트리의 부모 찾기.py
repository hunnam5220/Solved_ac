from sys import stdin
from collections import deque

n = int(stdin.readline())
arr = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, stdin.readline().split())
    arr[b].append(a)
    arr[a].append(b)

res = [[] for _ in range(n + 1)]


def bfs(root):
    q = deque()
    q.append(root)
    visited = set()
    visited.add(root)

    while q:
        now = q.popleft()
        for i in arr[now]:
            if i not in visited:
                res[i].append(now)
                visited.add(i)
                q.append(i)


bfs(1)
for i in range(2, n + 1):
    print(*res[i])