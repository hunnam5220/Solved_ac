from sys import stdin
n, m, k, start = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a - 1].append(b)

visited = [False] * n
tmp = [[] for _ in range(n)]


def bfs(start, k, visited):
    visited[start - 1] = True
    degree = 0
    tmp[degree].append(start)

    while k > degree:
        while tmp[degree]:
            idx = tmp[degree].pop()
            for x in graph[idx - 1]:
                if not visited[x - 1]:
                    tmp[degree + 1].append(x)
                    visited[x - 1] = True

        degree += 1


bfs(start, k, visited)

if len(tmp[k]) < 1:
    print(-1)
else:
    tmp[k].sort()

    for step in tmp[k]:
        print(step)


"""
12 11 5 8
1 2
1 3
2 4
2 7
3 8
3 9
4 5
4 6
7 11
8 10
9 12


"""