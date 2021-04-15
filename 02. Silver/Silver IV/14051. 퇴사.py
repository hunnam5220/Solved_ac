from sys import stdin

n = int(stdin.readline().rstrip())
t, p = [], []
max_val = 0
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    t.append(x)
    p.append(y)

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    time = t[i] + i

    if time <= n:
        dp[i] = max(max_val, dp[time] + p[i])
        max_val = dp[i]

    else:
        dp[i] = max_val

print(max_val)