from sys import stdin

n, k = map(int, stdin.readline().split())
graph = []
zero = [0]
for step in range(n):
    pp = list(map(int, stdin.readline().split()))
    zero[0] += pp.count(0)
    graph.append(pp)

tmp = [item[:] for item in graph]

s, x, y = map(int, stdin.readline().split())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def infection(number, nx, ny):
    for i in range(4):
        kx, ky = nx + dx[i], ny + dy[i]

        if (n > kx > -1 and n > ky > -1) and tmp[kx][ky] == 0:
            tmp[kx][ky] = number
            zero[0] -= 1


for step in range(s):
    for number in range(1, k + 1):
        for nx in range(n):
            for ny in range(n):
                if graph[nx][ny] == number:
                    infection(number, nx, ny)

        if zero[0] == 0:
            break
    graph = [item[:] for item in tmp]

print(tmp[x - 1][y - 1])
