from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

m, n, k = map(int, stdin.readline().split())
arr = []
for step in range(m):
    arr.append([0 for x in range(n)])

for step in range(k):
    x1, y1, x2, y2 = map(int, stdin.readline().rstrip().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[y][x] = 1


def dfs(x, y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False

    if arr[x][y] == 0:
        arr[x][y] = 1
        width.append(1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True

    return False


result = 0
width = []
w_result = []
for x in range(m):
    for y in range(n):
        if dfs(x, y):
            result += 1
            w_result.append(len(width))
            width = []

print(result)
w_result.sort()
print(' '.join(map(str, w_result)))