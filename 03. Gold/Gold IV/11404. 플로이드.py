from sys import stdin

n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())
INF = int(1e9)

dp = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            dp[i][j] = 0

for step in range(m):
    a, b, cost = map(int, stdin.readline().rstrip().split())
    if cost < dp[a - 1][b - 1]:
        dp[a - 1][b - 1] = cost

for k in range(n):
    for a in range(n):
        for b in range(n):
            dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])

for a in dp:
    for b in a:
        if b == INF:
            print(0, end=' ')
        else:
            print(b, end=' ')
    print()
