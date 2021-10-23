from sys import stdin

n, m = map(int, stdin.readline().split())
arr = []
for i in range(n):
    data = list(map(int, stdin.readline().split()))
    for j in range(1, n):
        data[j] += data[j-1]
    arr.append(data)

for _ in range(m):
    res = 0
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    for i in range(x1-1, x2):
        if y1 - 2 > -1:
            res += (arr[i][y2-1] - arr[i][y1-2])
        else:
            res += (arr[i][y2-1])

    print(res)