from sys import stdin


def solve(graph, root):
    dist = {}
    for node in graph:
        dist[node] = int(2e9)
    dist[root] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neigh in graph[node]:
                if dist[neigh] > dist[node] + graph[node][neigh]:
                    dist[neigh] = dist[node] + graph[node][neigh]

    for node in graph:
        for neigh in graph[node]:
            if dist[neigh] > dist[node] + graph[node][neigh]:
                return True

    return False


for _ in range(int(stdin.readline())):
    n, m, w = map(int, stdin.readline().split())
    graph = {}

    for __ in range(m):
        s, e, t = map(int, stdin.readline().split())
        if s not in graph:
            graph[s] = {}

        if e in graph[s]:
            if graph[s][e] > t:
                graph[s][e] = t
        else:
            graph[s][e] = t

        if e not in graph:
            graph[e] = {}

        if s in graph[e]:
            if graph[e][s] > t:
                graph[e][s] = t
        else:
            graph[e][s] = t

    for __ in range(w):
        s, e, t = map(int, stdin.readline().split())
        if s not in graph:
            graph[s] = {}

        if e in graph[s]:
            if graph[s][e] > -t:
                graph[s][e] = -t
        else:
            graph[s][e] = -t

    if solve(graph, 1) is True:
        print('YES')
    else:
        print('NO')
