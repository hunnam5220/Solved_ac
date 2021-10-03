from sys import stdin

result = 0


def solve(n, x, y):
    global result
    if x == r and y == c:
        print(result)
        return

    if n == 1:
        result += 1
        return

    if not (x <= r < x + n and y <= c < y + n):
        result += n * n
        return
    solve(n // 2, x, y)
    solve(n // 2, x, y + n // 2)
    solve(n // 2, x + n // 2, y)
    solve(n // 2, x + n // 2, y + n // 2)


n, r, c = map(int, stdin.readline().split())
# (0, 0) 부터 시작해
solve(2 ** n, 0, 0)