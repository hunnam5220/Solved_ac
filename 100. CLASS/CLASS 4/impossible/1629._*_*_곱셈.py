from sys import stdin

a, b, c = map(int, stdin.readline().split())


def solve(a, b, c):
    if b == 1:
        return a
    temp = solve(a, b // 2, c)
    if b % 2 == 0:
        return temp * temp % c
    else:
        return temp * temp * a % c


print(solve(a, b, c) % c)