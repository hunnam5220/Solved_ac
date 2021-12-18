from sys import stdin

n, m, k = map(int, stdin.readline().split())
ans = -int(1e9)
arr = []
for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
visited = [[True] * m for _ in range(n)]


def solve(cnt, res, px, py):
    global ans
    if cnt == k:
        ans = max(ans, res)
        return

    else:
        for i in range(px, n):
            # i 가 px 라면 py부터 찾고, 아니라면 0부터 찾아
            for j in range(py if px == i else 0, m):
                if visited[i][j] is False:
                    continue

                in_tf = True
                for idx in range(4):
                    nx, ny = i + dx[idx], j + dy[idx]
                    if -1 < nx < n and -1 < ny < m:
                        if visited[nx][ny] is False:
                            in_tf = False
                            break

                if in_tf:
                    visited[i][j] = False
                    solve(cnt + 1, res + arr[i][j], i, j)
                    visited[i][j] = True


solve(0, 0, 0, 0)
print(ans)
