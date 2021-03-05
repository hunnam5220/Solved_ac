import sys
from copy import deepcopy
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline().rstrip())
arr = []
rain = []
m = 1


def dfs(x, y, graph, v):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if graph[x][y] > v:
        graph[x][y] = 0
        dfs(x - 1, y, graph, v)
        dfs(x, y - 1, graph, v)
        dfs(x + 1, y, graph, v)
        dfs(x, y + 1, graph, v)

        return True

    return False


for step in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.append(tmp)
    rain.extend(tmp)

rain = list(set(rain))

for v in rain:
    result = 0
    graph = deepcopy(arr)

    for x in range(n):
        for y in range(n):
            if dfs(x, y, graph, v):
                result += 1

    if result > m:
        m = result

print(m)