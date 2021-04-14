from sys import stdin

n = int(stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(list(map(int, stdin.readline().rstrip().split())))

dp = [item[:] for item in arr]
start = arr[0][0]

for i in range(1, n):
    for j in range(len(arr[i])):
        if i == 1:
            dp[i][j] = dp[i][j] + dp[i - 1][0]

        elif j == 0:
            dp[i][j] = dp[i][j] + dp[i - 1][0]

        elif j == len(arr[i]) - 1:
            dp[i][j] = dp[i][j] + dp[i - 1][j - 1]

        else:
            dp[i][j] = max(dp[i - 1][j] + dp[i][j], dp[i - 1][j - 1] + dp[i][j])

print(max(dp[-1]))


"""
5
1
1 1
1 0 1
1 0 0 1
1 0 100 0 1
"""