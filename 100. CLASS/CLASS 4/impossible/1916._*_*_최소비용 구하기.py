from sys import stdin
import heapq

n, m = int(stdin.readline()), int(stdin.readline())
arr = [[] for _ in range(n + 1)]
for i in range(m):
    start, goal, cost = map(int, stdin.readline().split())
    arr[start].append((cost, goal))
dist = [int(1e9) for _ in range(n + 1)]


a, b = map(int, stdin.readline().split())


def djikstra():
    q = []
    heapq.heappush(q, (0, a))

    while q:
        cost, n = heapq.heappop(q)
        if dist[n] < cost:
            continue

        for c, node in arr[n]:
            n_cost = cost + c
            if dist[node] > n_cost:
                dist[node] = n_cost
                heapq.heappush(q, (n_cost, node))


djikstra()
print(dist[b])