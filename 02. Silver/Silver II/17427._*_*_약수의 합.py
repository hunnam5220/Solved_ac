from sys import stdin

inf = int(1e6)
dp = [1 for _ in range(inf + 1)]
s = [0 for _ in range(inf + 1)]

n = int(stdin.readline())

for i in range(2, n + 1):
    j = 1

    while i * j <= n:
        dp[i * j] += i
        j += 1


for i in range(1, n + 1):
    s[i] = s[i - 1] + dp[i]

print(s[n])