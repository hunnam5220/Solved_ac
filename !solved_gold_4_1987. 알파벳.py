# BFS

from sys import stdin, setrecursionlimit
setrecursionlimit(1000)

r, c = map(int, stdin.readline().rstrip().split())

arr = []
visited = []
for step in range(r):
    arr.append(list(stdin.readline().rstrip()))


def dfs(x, y, visited):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False

    if arr[x][y] not in visited:
        visited.append(arr[x][y])
        dfs(x, y - 1, visited)
        dfs(x - 1, y, visited)
        dfs(x + 1, y, visited)
        dfs(x, y + 1, visited)
        return True

    visited.pop()
    return False


result = 0
dfs(0, 0, visited)
print(len(visited))