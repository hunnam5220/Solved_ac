from sys import stdin

n = int(stdin.readline())
arr = [x for x in range(n)]
board = []
ans = int(1e11)
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))


def solve(start, k, res):
    if len(visited) == n:
        global ans
        if board[visited[-1]][start] != 0:
            res += board[visited[-1]][start]
            ans = min(ans, res)
        return

    for i in range(n):
        if i not in visited and board[k][i] != 0:
            visited.append(i)
            solve(start, i, res + board[k][i])
            visited.pop()


for i in range(n):
    visited = [i]
    solve(i, i, 0)

print(ans)


