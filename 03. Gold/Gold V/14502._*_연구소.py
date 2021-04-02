from sys import stdin

n, m = map(int, stdin.readline().split())
graph = []

for step in range(n):
    graph.append(list(map(int, stdin.readline().split())))

tmp = [item[:] for item in graph]
result = [0]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def get_area_zero():
    cnt = 0
    for x in range(n):
        for y in range(m):
            if tmp[x][y] == 0:
                cnt += 1
    return cnt


def infection(x, y):
    """ 바이러스 퍼지게 하기 """
    for step in range(4):
        nx = x + dx[step]
        ny = y + dy[step]

        if n > nx >= 0 and m > ny >= 0:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                infection(nx, ny)


def install(count):
    """ 울타리 설치하기 """
    if count == 3:
        for x in range(n):
            for y in range(m):
                tmp[x][y] = graph[x][y]

        for x in range(n):
            for y in range(m):
                if tmp[x][y] == 2:
                    infection(x, y)

        result[0] = max(result[0], get_area_zero())
        return

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                graph[x][y] = 1
                count += 1
                install(count)
                graph[x][y] = 0
                count -= 1


install(0)
print(result[0])
