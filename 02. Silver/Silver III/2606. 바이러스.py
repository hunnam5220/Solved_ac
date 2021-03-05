from sys import stdin

n = int(stdin.readline().rstrip())
k = int(stdin.readline().rstrip())
arr = [[] for _ in range(n + 1)]
for step in range(k):
    x, y = map(int, stdin.readline().split())
    arr[x - 1].append(y)
    arr[y - 1].append(x)

for step in arr:
    step.sort()


def dfs(arr, root_node, visited):
    visited[root_node - 1] = True

    for step in arr[root_node - 1]:
        if not visited[step - 1]:
            dfs(arr, step, visited)


visited = [False] * len(arr)
dfs(arr, 1, visited)
result = [x for x in visited if x is True]
print(len(result) - 1)