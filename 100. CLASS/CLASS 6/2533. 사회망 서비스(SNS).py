from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 8)

n = int(stdin.readline())
nodes = [[] for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)


def dfs(r):
    visited[r] = 1
    dp[r][0] = 1

    for i in nodes[r]:
        if not visited[i]:
            dfs(i)
            dp[r][0] += min(dp[i][0],dp[i][1])
            dp[r][1] += dp[i][0]


dfs(1)
print(min(dp[1]))
