from sys import stdin

n, m = map(int, stdin.readline().split())
arr = []
psum = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        psum[i][j] = psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1] + arr[i-1][j-1]

res = -int(4e9) -1
for x1 in range(1, n + 1):
    for y1 in range(1, m + 1):
        for x2 in range(x1, n + 1):
            for y2 in range(y1, m + 1):
                res = max(res, psum[x2][y2] - psum[x2][y1-1] - psum[x1-1][y2] + psum[x1-1][y1-1])

print(res)