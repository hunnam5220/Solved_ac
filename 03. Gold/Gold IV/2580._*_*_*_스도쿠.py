from sys import stdin

board = []
zero_xy = []

for i in range(9):
    data = list(map(int, stdin.readline().split()))
    board.append(data)
    for j in range(9):
        if data[j] == 0:
            zero_xy.append((i, j))


def check_row(x, i):
    for k in board[x]:
        if i == k:
            return False
    return True


def check_col(y, i):
    for k in range(9):
        if board[k][y] == i:
            return False
    return True


def chekc_33_box(x, y, i):
    nx, ny = x // 3 * 3, y // 3 * 3
    for k in range(3):
        for p in range(3):
            if board[k + nx][p + ny] == i:
                return False

    return True


def solve(cnt):
    if cnt == len(zero_xy):
        for r in board:
            print(*r)
        exit()

    for i in range(1, 10):
        x = zero_xy[cnt][0]
        y = zero_xy[cnt][1]

        if check_row(x, i) and check_col(y, i) and chekc_33_box(x, y, i):
            board[x][y] = i
            solve(cnt + 1)
            board[x][y] = 0


solve(0)