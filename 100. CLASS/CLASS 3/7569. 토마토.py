from sys import stdin
from collections import deque

m, n, h = map(int, stdin.readline().split())
arr = []
tomato = []
dx, dy = [1, 0, 0, -1, 0, 0], [0, 1, -1, 0, 0, 0]
zero = 0
visited = set()

for k in range(h):
    temp = []
    for i in range(n):
        data = list(map(int, stdin.readline().split()))
        for j in range(m):
            if data[j] == 1:
                tomato.append((0, k, i, j))
            elif data[j] == 0:
                zero += 1
        temp.append(data)
    arr.append(temp)


def bfs():
    q = deque()
    q.extend(tomato)
    cost = 0

    while q:
        cost, f, x, y = q.popleft()

        for i in range(6):
            if i == 4:
                nf, nx, ny = f - 1, x, y
            elif i == 5:
                nf, nx, ny = f + 1, x, y
            else:
                nf, nx, ny = f, x + dx[i], y + dy[i]

            if -1 < nf < h and -1 < nx < n and -1 < ny < m:
                if arr[nf][nx][ny] == 0:
                    arr[nf][nx][ny] = 1
                    visited.add((nf, nx, ny))
                    q.append((cost + 1, nf, nx, ny))

    return cost


if zero > 0:
    res = bfs()
    if zero - len(visited) != 0:
        print(-1)
    else:
        print(res)


else:
    print(0)