from sys import stdin

n = int(stdin.readline())
dp = [0, 1, 1]
for i in range(3, 41):
    dp.append(dp[i - 2] + dp[i - 1])

ans = [dp[n], 0]
if 0 < n < 3:
    ans[1] = 1
else:
    ans[1] = n - 2

print(*ans)