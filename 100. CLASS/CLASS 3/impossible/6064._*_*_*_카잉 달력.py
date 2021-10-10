from sys import stdin


def solve(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1


for _ in range(int(stdin.readline())):
    m, n, x, y = map(int, stdin.readline().split())
    print(solve(m, n, x, y))
