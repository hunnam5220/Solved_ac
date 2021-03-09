# BFS

from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

n = int(stdin.readline().rstrip())
arr = [[] for _ in range(n)]
result = []


for step in range(n - 1):
    x, y = map(int, stdin.readline().split())
    arr[x - 1].append(y)
    arr[y - 1].append(x)


def dfs(arr, v, result):
    stack = [v]

    while stack:
        break

dfs(arr, 1, result)