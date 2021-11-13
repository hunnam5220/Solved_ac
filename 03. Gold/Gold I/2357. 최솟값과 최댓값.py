from sys import stdin

inf = int(1e9)
n, m = map(int, stdin.readline().split())
mtree = [inf for _ in range(n * 4)]
xtree = [-inf for _ in range(n * 4)]
x = 1
while x < n:
    x *= 2

for i in range(n):
    data = int(stdin.readline())
    mtree[x + i] = data
    xtree[x + i] = data

for i in range(x - 1, 0, -1):
    xtree[i] = max(xtree[i * 2], xtree[i * 2 + 1])
    mtree[i] = min(mtree[i * 2], mtree[i * 2 + 1])


def find(l, r, mode):
    l += x
    r += x
    res = inf if mode == 0 else -inf

    while l <= r:
        if l % 2 == 1:
            res = min(res, mtree[l]) if mode == 0 else max(res, xtree[l])

        if r % 2 == 0:
            res = min(res, mtree[r]) if mode == 0 else max(res, xtree[r])

        l = (l + 1) // 2
        r = (r - 1) // 2

    return res


for _ in range(m):
    a, b = map(int, stdin.readline().split())
    print(find(a - 1, b - 1, 0), find(a - 1, b - 1, 1))