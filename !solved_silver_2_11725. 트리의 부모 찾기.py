from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

n = int(stdin.readline().rstrip())
arr = [[] for _ in range(n)]
result = []


for step in range(n - 1):
    x, y = map(int, stdin.readline().split())
    arr[x - 1].append(y)
    arr[y - 1].append(x)


def dfs(arr, v, visited):
    visited[v - 1] = True
    result.append(v)

    for step in arr[v - 1]:
        if not visited[step - 1]:
            dfs(arr, step, visited)


visited = [False] * n
dfs(arr, 1, visited)

for step in range(2, n + 1):
    print(result[result.index(step) - 1])