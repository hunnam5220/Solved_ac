import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [[] for _ in range(n)]

for step in range(m):
    x, y = map(int, sys.stdin.readline().split())
    arr[x - 1].append(y)
    arr[y - 1].append(x)


def dfs(arr, root_node, visited):
    if not visited[root_node - 1]:
        visited[root_node - 1] = True

        for step in arr[root_node - 1]:
            if not visited[step - 1]:
                dfs(arr, step, visited)
        return True
    else:
        return False


result = 0
visited = [False] * n
root_node = 1
for k in range(1, n + 1):
    if dfs(arr, k, visited):
        result += 1
print(result)