from sys import stdin, setrecursionlimit
setrecursionlimit(10000000)
from copy import deepcopy

n = int(stdin.readline().rstrip())
arr = []
for step in range(n):
    arr.append(list(stdin.readline().rstrip()))

nr_arr = deepcopy(arr)

for x in range(n):
    for y in range(n):
        if arr[x][y] == 'R' or arr[x][y] == 'G':
            arr[x][y] = 1
        if arr[x][y] == 'B':
            arr[x][y] = 2

for x in range(n):
    for y in range(n):
        if nr_arr[x][y] == 'R':
            nr_arr[x][y] = 1
        elif nr_arr[x][y] == 'G':
            nr_arr[x][y] = 2
        if nr_arr[x][y] == 'B':
            nr_arr[x][y] = 3


def dfs(x, y, chk, normal=True):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if normal and nr_arr[x][y] == chk:
        nr_arr[x][y] = 9
        dfs(x - 1, y, chk)
        dfs(x, y - 1, chk)
        dfs(x + 1, y, chk)
        dfs(x, y + 1, chk)

        return True

    elif not normal and arr[x][y] == chk:
        arr[x][y] = 9
        dfs(x - 1, y, chk, False)
        dfs(x, y - 1, chk, False)
        dfs(x + 1, y, chk, False)
        dfs(x, y + 1, chk, False)

        return True

    return False


nr, rg = 0, 0
for chk in range(1, 4):
    for x in range(n):
        for y in range(n):
            if dfs(x, y, chk):
                nr += 1

            if dfs(x, y, chk, False):
                rg += 1

print(nr, rg)