from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

n = int(stdin.readline().rstrip())
arr = [[] for _ in range(n)]

for step in range(n - 1):
    x, y = map(int, stdin.readline().split())
    arr[x - 1].append(y)
    arr[y - 1].append(x)


def dfs(arr, v):
    for step in arr[v-1]:
        print(step)
        break


for v in range(2, n + 1):
    dfs(arr, v)