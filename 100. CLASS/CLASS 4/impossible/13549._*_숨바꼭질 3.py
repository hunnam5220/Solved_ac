from collections import deque


def bfs():
    q = deque()  
    q.append(n)  
    while q:
        x = q.popleft()  
        if x == k:
            print(dist[x])
            break
        for nx in (x * 2, x - 1, x + 1):
            if 0 <= nx <= MAX and not dist[nx]:
                if nx != x * 2:
                    dist[nx] = dist[x] + 1
                else:
                    dist[nx] = dist[x]
                q.append(nx)


MAX = 10 ** 5 + 1
dist = [0] * (MAX + 1)  
n, k = map(int, input().split())

bfs()
