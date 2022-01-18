from sys import stdin
from collections import deque

dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
n, m = map(int, stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))
island = [set() for _ in range(9)]
inf = int(1e9)


def install_bridge(direction, x, y, island_num):
    bridge = set()
    while 1:
        x += dx[direction]
        y += dy[direction]
        if 0 <= x < n and 0 <= y < m:
            if arr[x][y] == island_num:
                return False

            elif arr[x][y] == 0:
                bridge.add((x, y))

            else:
                if len(bridge) < 2:
                    return False
                break
        else:
            return False


def bfs(x, y, i_num):
    q = deque()
    q.append((x, y))
    visited = set()
    visited.add((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = i_num
                    q.append((nx, ny))
                    visited.add((nx, ny))

    return visited


island_num = 2
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            island_xy = bfs(i, j, island_num)
            island[island_num].update(island_xy)
            island_num += 1

for i in range(2, island_num):
    if island[i]:
        for x, y in island[i]:
            for direction in range(4):
                install_bridge(direction, x, y, i)

