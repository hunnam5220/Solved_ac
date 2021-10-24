from sys import stdin

n = int(stdin.readline())
arr = [[0] * (n + 1)]
for i in range(n):
    arr.append([0] + list(map(int, stdin.readline().split())))

psum1 = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        psum1[i][j] = arr[i][j] + psum1[i - 1][j - 1]

psum2 = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n+1):
    for j in range(1, n + 1):
        if j != n:
            psum2[i][j] = arr[i][j] + psum2[i - 1][j + 1]
        else:
            psum2[i][j] = arr[i][j]

ans = 0
for length in range(2, n + 1):
    for r in range(2, n + 1):
        for c in range(2, n + 1):
            if r - length + 1 <= 0 or c - length + 1 <= 0:
                continue

            psum1_val = psum1[r][c]
            if 0 < r - length < n + 1 and 0 < c - length < n + 1:
                psum1_val -= psum1[r - length][c - length]

            psum2_val = psum2[r][c - length + 1]
            if 0 < r - length < n + 1 and 0 < c + 1 < n + 1:
                psum2_val -= psum2[r - length][c + 1]

            ans = max(ans, psum1_val - psum2_val)

print(ans)