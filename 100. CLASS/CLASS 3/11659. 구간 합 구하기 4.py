from sys import stdin

n, m = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
dp = [0, a[0]]
for i in range(2, n + 1):
    dp.append(a[i-1] + dp[i - 1])

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    print(dp[b] - dp[a - 1])