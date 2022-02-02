from sys import stdin
from bisect import bisect_left

dp = [1 for _ in range(1000)]
dp[1], dp[2] = 1, 2
for i in range(3, 1000):
    dp[i] = (dp[i - 2] + dp[i - 1])

while 1:
    a, b = map(int, stdin.readline().split())
    if a == 0 and b == 0:
        break

    l = bisect_left(dp, a)
    ans = 0
    for i in range(1, 1000):
        if a <= dp[i] <= b:
            ans += 1

    print(ans)

