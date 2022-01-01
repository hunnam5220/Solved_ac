from sys import stdin


def solve(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return solve(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = solve(a, b, c - 1) + solve(a, b - 1, c - 1) - solve(a, b - 1, c)
        return dp[a][b][c]

    dp[a][b][c] = solve(a - 1, b, c) + solve(a - 1, b - 1, c) + solve(a - 1, b, c - 1) - solve(a - 1, b - 1, c - 1)
    return dp[a][b][c]


dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]


while 1:
    a, b, c = map(int, stdin.readline().split())
    if a == b == c == -1:
        break
    ans = solve(a, b, c)
    print('w({}, {}, {}) = {}'.format(a, b, c, ans))