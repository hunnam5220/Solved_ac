import sys
sys.setrecursionlimit(10000)


def dfs(x, y):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False

    if arr[x][y] == 1:
        arr[x][y] = 0

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        dfs(x + 1, y + 1)
        dfs(x + 1, y - 1)
        dfs(x - 1, y + 1)
        dfs(x - 1, y - 1)

        return True

    return False


while 1:
    w, h = map(int, sys.stdin.readline().split())
    if w == h == 0:
        break

    arr = []
    result = 0

    for step in range(h):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

    for x in range(h):
        for y in range(w):
            if dfs(x, y):
                result += 1
    print(result)