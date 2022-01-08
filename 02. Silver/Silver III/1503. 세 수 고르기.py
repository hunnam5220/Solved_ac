from sys import stdin

n, m = map(int, stdin.readline().split())
arr = []
if m > 0:
    arr = list(map(int, stdin.readline().split()))

ans = int(1e9)

for i in range(1, 1001):
    if i in arr:
        continue
    for j in range(i, 1001):
        if j in arr:
            continue
        for k in range(j, 1002):
            if k in arr:
                continue
            ans = min(ans, abs(n - i * j * k))
print(ans)