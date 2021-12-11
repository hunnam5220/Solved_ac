from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
tree = [0 for _ in range(n * 4)]
x = 1

while n > x:
    x *= 2

for i in range(n):
    tree[x + i] = arr[i]

for i in range(x - 1, 0, -1):
    tree[i] = max(tree[i * 2], tree[i * 2 + 1])


def get_max(l, r):
    l += x
    r += x
    res = -int(1e9)

    while l <= r:
        if l % 2 == 1:
            res = tree[l] if res < tree[l] else res

        if r % 2 == 0:
            res = tree[r] if res < tree[r] else res

        l = (l + 1) // 2
        r = (r - 1) // 2

    return res


ans = []
for i in range(m - 1, n - m + 1):
    l, r = i - (m - 1), i + (m - 1)
    ans.append(get_max(l, r))

print(*ans)