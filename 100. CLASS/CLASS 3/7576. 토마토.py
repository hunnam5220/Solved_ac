from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
arr = []
data = []
visited = set()

for i in range(m):
    temp = list(map(int, stdin.readline().split()))
    arr.append(temp)
    for j in range(n):
        if temp[j] == 1:
            data.append((0, i, j))
            visited.add((i, j))

dx, dy = [1,0,0,-1], [0,1,-1,0]
res = 0


def bfs(cost, a, b):
    q = deque()
    q.extend(data)
    p = 0

    while q:
        cost, a, b = q.popleft()
        if cost > p:
            p = cost

        for i in range(4):
            nx, ny = dx[i] + a, dy[i] + b
            if -1<nx<m and -1<ny<n :
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    q.append((cost+1, nx, ny))
                    visited.add((nx, ny))
    return p

res += bfs(0, i, j)

def check():
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                return False
    return True

if check():
    print(res)
else:
    print(-1)