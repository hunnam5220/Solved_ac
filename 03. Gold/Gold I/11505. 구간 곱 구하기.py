from sys import stdin

n, m, k = map(int, stdin.readline().split())

tree = [1 for _ in range(n * 4)]

x = 1
while x < n:
    x *= 2

for i in range(n):
    tree[i + x] = int(stdin.readline())

for i in range(x - 1, 0, -1):
    tree[i] = (tree[i * 2] * tree[i * 2 + 1]) % 1000000007


def change(l, c):
    l += x
    tree[l] = c
    l //= 2

    while l > 0:
        tree[l] = (tree[l * 2] * tree[l * 2 + 1]) % 1000000007
        l //= 2


def mul(l, r):
    l += x
    r += x
    res = 1

    while l <= r:
        if l % 2 == 1:
            res *= tree[l]
            res %= 1000000007

        if r % 2 == 0:
            res *= tree[r]
            res %= 1000000007

        l = (l + 1) // 2
        r = (r - 1) // 2

    return res


for _ in range(m + k):
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        change(b - 1, c)
    else:
        print(mul(b - 1, c - 1))
