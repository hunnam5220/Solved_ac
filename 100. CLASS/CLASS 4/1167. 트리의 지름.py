from collections import deque
from sys import stdin

n = int(stdin.readline())
graph = [set() for _ in range(n + 1)]
max_dist = 0

# 데이터 전처리
for _ in range(n):
    data = list(map(int, stdin.readline().split()))

    node = data[0]
    length = len(data)
    to_node, cost = 1, 2
    for _ in range((length - 2) // 2):
        if data[to_node] not in graph[node]:
            graph[node].add((data[to_node], data[cost]))
            graph[data[to_node]].add((node, data[cost]))

        to_node += 2
        cost += 2


# 탐색
def bfs(root):
    global max_dist
    q = deque()
    q.append((root, 0))
    visited = set()
    visited.add(root)
    res = (0, 0)

    while q:
        now, dist = q.popleft()
        for node, cost in graph[now]:
            if node not in visited:
                q.append((node, cost + dist))
                visited.add(node)
                if cost + dist > res[1]:
                    res = (node, cost + dist)

    return res


# 실행
root = bfs(1)
res = bfs(root[0])
print(res[1])