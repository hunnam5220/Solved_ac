from sys import stdin

n = int(stdin.readline())
dp = []
for i in range(n):
    dp.append(list(map(int, stdin.readline().split())))

for i in range(1, n):
    for j in range(n):
        if j == 0:
            dp[i][j] = min(dp[i][j] + dp[i-1][1], dp[i][j] + dp[i-1][2])
        if j == 1:
            dp[i][j] = min(dp[i][j] + dp[i-1][0], dp[i][j] + dp[i-1][2])
        if j == 2:
            dp[i][j] = min(dp[i][j] + dp[i-1][0], dp[i][j] + dp[i-1][1])

print(min(dp[n-1]))

"""
3
26 40 83
49 60 57
13 89 99
"""