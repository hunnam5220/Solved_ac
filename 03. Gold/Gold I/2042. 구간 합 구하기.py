from sys import stdin

n, m, k = map(int, stdin.readline().split())
tree = [0 for _ in range(n * 4)]
x = 1

while x < n:
    x *= 2

for i in range(n):
    tree[x + i] = int(stdin.readline())

for i in range(x - 1, 0, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]


def change(f, t):
    f += x
    tree[f] = t
    f //= 2
    while f > 0:
        tree[f] = tree[f * 2] + tree[f * 2 + 1]
        f //= 2


def deohagi(l, r):
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


for _ in range(m + k):
    a, b, c = map(int, stdin.readline().split())

    if a == 1:
        change(b-1, c)

    else:
        print(deohagi(b-1, c-1))