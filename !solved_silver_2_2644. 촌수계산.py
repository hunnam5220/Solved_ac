from sys import stdin, setrecursionlimit
setrecursionlimit(10000000)

n = int(stdin.readline().rstrip())
a, b = map(int, stdin.readline().split())
m = int(stdin.readline().rstrip())
arr = [[] for _ in range(n)]

for step in range(m):
    x, y = map(int, stdin.readline().split())
    arr[x - 1].append(y)
    arr[y - 1].append(x)
result = []
chk = [False]


def dfs(arr, a, visited):
    visited[a - 1] = True
    if len(arr[a - 1]) == 1 and b not in arr[a - 1] and len(result) > 1 and len(arr[a]) == 1:
        result.pop()
    else:
        result.append(a)

    if b == a:
        chk[0] = True
        return

    if b not in arr[a - 1]:
        for step in arr[a - 1]:
            if not visited[step - 1] and not chk[0]:
                dfs(arr, step, visited)

    else:
        result.append(b)
        chk[0] = True


visited = [False] * n
dfs(arr, a, visited)


if chk[0]:
    print(len(result) - 1)
else:
    print(-1)