from collections import deque
from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    n = int(stdin.readline().rstrip())
    indegree = [0] * (n + 1)

    graph = [[False] * (n + 1) for _ in range(n + 1)]

    last_year_grade = list(map(int, stdin.readline().split()))

    for i in range(n):
        for j in range(i + 1, n):
            graph[last_year_grade[i]][last_year_grade[j]] = True
            indegree[last_year_grade[j]] += 1

    m = int(stdin.readline().rstrip())
    for _ in range(m):
        a, b = map(int, stdin.readline().split())

        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1

        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break

        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)

        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")

    elif not certain:
        print("?")

    else:
        for i in result:
            print(i, end=' ')
        print()
