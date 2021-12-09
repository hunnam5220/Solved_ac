from collections import deque
from sys import stdin


r, c, n = map(int, stdin.readline().split())
board = []
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
pre = set()
now = set()
for i in range(r):
    data = list(stdin.readline().rstrip())
    for j in range(c):
        if data[j] == 'O':
            pre.add((i, j))
    board.append(data)


def install_bomb():
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                board[i][j] = 'O'
                now.add((i, j))


def bomb(bombs, now):
    for x, y in bombs:
        board[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < r and -1 < ny < c:
                if board[nx][ny] == 'O':
                    board[nx][ny] = '.'
                    now.discard((nx, ny))


for time in range(1, n + 1):
    if time == 1:
        continue

    if time % 2 == 0:
        install_bomb()

    elif time % 2 == 1:
        bomb(pre, now)
        pre = now
        now = set()

for i in board:
    print(*i, sep='')

"""
4 4 10
...O
....
O...
....
"""