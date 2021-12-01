from sys import stdin

n = int(stdin.readline())
dp = [list(map(int, stdin.readline().split())) for _ in range(n)]
res = [[[0 for _ in range(n)] for __ in range(n)] for ___ in range(3)]
res[0][0][1] = 1

for i in range(2, n):
    if dp[0][i] == 0:
        res[0][0][i] = res[0][0][i - 1]

for i in range(1, n):
    for j in range(2, n):
        if dp[i][j] == 0 and dp[i - 1][j] == 0 and dp[i][j - 1] == 0:
            res[2][i][j] = res[0][i - 1][j - 1] + res[1][i - 1][j - 1] + res[2][i - 1][j - 1]

        if dp[i][j] == 0:
            res[0][i][j] = res[0][i][j - 1] + res[2][i][j - 1]
            res[1][i][j] = res[1][i - 1][j] + res[2][i - 1][j]

print(res[0][n-1][n-1] + res[1][n-1][n-1] + res[2][n-1][n-1])
