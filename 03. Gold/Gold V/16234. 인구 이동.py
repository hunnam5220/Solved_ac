from sys import stdin
from collections import deque

# 너비 우선 탐색 적용
n, l, r = map(int, stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(index, x, y):
    united = [(x, y)]

    q = deque()
    q.append((x, y))
    chk[x][y] = index
    cnt = 1
    summary = arr[x][y]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n and 0 <= ny < n) and chk[nx][ny] == -1:
                if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                    q.append((nx, ny))
                    chk[nx][ny] = index
                    summary += arr[nx][ny]
                    cnt += 1
                    united.append((nx, ny))

    for i, j in united:
        arr[i][j] = summary // cnt


total = 0

while 1:
    chk = [[-1] * n for _ in range(n)]
    index = 0

    for x in range(n):
        for y in range(n):
            if chk[x][y] == -1:
                bfs(index, x, y)
                index += 1

    if index == n * n:
        break

    total += 1

print(total)