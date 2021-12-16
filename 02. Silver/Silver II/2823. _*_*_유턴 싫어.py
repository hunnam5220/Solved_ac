from collections import deque
from sys import stdin

r, c = map(int, stdin.readline().split())
arr, roads, dx, dy = [], [], [1, 0, 0, -1], [0, 1, -1, 0]
for i in range(r):
    data = list(stdin.readline().rstrip())
    arr.append(data)
    for j in range(c):
        if data[j] == '.':
            roads.append((i, j))


def solve(x, y):
    q = deque()
    q.append((x, y))
    visited = set()

    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1 < nx < r and -1 < ny < c:
                if arr[nx][ny] == '.':
                    cnt += 1

                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))

        if cnt < 2:
            return 1

    return 0


for x, y in roads:
    if solve(x, y) == 0:
        print(0)
        exit()
print(1)