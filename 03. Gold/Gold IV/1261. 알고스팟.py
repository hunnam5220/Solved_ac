import heapq
from sys import stdin

m, n = map(int, stdin.readline().split())
board, dx, dy = [], [1, 0, 0, -1], [0, -1, 1, 0]
ans = int(1e9)

for _ in range(n):
    board.append(list(map(int, list(stdin.readline().rstrip()))))


def solve():
    global ans
    q = []
    heapq.heappush(q, (0, 0, 0))
    visited = set()
    visited.add((0, 0))

    while q:
        cnt, x, y = heapq.heappop(q)

        if (x, y) == (n - 1, m - 1):
            ans = min(ans, cnt)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1 < nx < n and -1 < ny < m:
                if (nx, ny) not in visited:
                    if board[nx][ny] == 1:
                        heapq.heappush(q, (cnt + 1, nx, ny))
                    else:
                        heapq.heappush(q, (cnt, nx, ny))

                visited.add((nx, ny))


solve()
print(ans)
