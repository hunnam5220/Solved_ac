from sys import stdin, setrecursionlimit
setrecursionlimit(10000000)

n, m = map(int, stdin.readline().rstrip().split())
arr = []
for step in range(n):
    arr.append(list(map(int, stdin.readline().rstrip().split())))
result, year = 0, 0
remove = [[0 for x in range(m)] for _ in range(n)]


def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if tmp[x][y] != 0:
        try:
            if arr[x + 1][y] == 0:
                remove[x][y] += 1
            if arr[x][y + 1] == 0:
                remove[x][y] += 1
            if arr[x - 1][y] == 0:
                remove[x][y] += 1
            if arr[x][y - 1] == 0:
                remove[x][y] += 1
        except:
            pass

        tmp[x][y] = 0
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)

        return True

    return False


while 1:
    tmp = [item[:] for item in arr]
    remove = [item[:] for item in arr]

    year += 1
    result = '0'
    for x in range(n):
        for y in range(m):
            remove[x][y] = 0
            if dfs(x, y):
                result = int(result) + 1

            arr[x][y] -= remove[x][y]
            if arr[x][y] < 0:
                arr[x][y] = 0

    if result == '0':
        print(result)
        break

    elif result >= 2:
        print(year - 1)
        break


