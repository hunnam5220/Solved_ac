from sys import stdin

n = int(stdin.readline())
dp = [0 for _ in range(1000)]
dp[0] = 1
dp[1] = 3
for i in range(2, n):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

print(dp[n-1] % 10007)