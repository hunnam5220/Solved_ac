from sys import stdin

n, m = map(int, stdin.readline().split())
tree = [0 for _ in range(n * 4)]
x = 1
while x < n:
    x *= 2


def change(f, t):
    f += x
    tree[f] = t
    f //= 2
    while f > 0:
        tree[f] = tree[f * 2] + tree[f * 2 + 1]
        f //= 2


def get_value(l, r):
    l += x
    r += x
    res = 0

    while l <= r:
        if l % 2 == 1:
            res += tree[l]

        if r % 2 == 0:
            res += tree[r]

        l = (l + 1) // 2
        r = (r - 1) // 2

    return res


for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        change(b - 1, c)

    else:
        if b <= c:
            print(get_value(b - 1, c - 1))
        else:
            print(get_value(c - 1, b - 1))