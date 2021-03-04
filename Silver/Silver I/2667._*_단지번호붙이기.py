from sys import stdin

n = int(stdin.readline().rstrip())
graph = []
for step in range(n):
    graph.append(list(map(int, stdin.readline().rstrip())))


def dfs(x, y):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        k.append(1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False


result = 0
arr = []
for x in range(n):
    for y in range(n):
        k = []
        if dfs(x, y):
            result += 1
            arr.append(len(k))

print(result)
arr.sort()
print('\n'.join(map(str, arr)))