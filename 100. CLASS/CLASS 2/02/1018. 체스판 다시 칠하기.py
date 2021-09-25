from sys import stdin

n, m = map(int, stdin.readline().split())
board = []
for i in range(n):
    board.append(list(stdin.readline().rstrip()))

res = int(1e9)


def check(test_board, pre_color):
    temp = 0

    if test_board[0][0] != pre_color:
        test_board[0][0] = pre_color
        temp += 1

    for i in range(0, 8):
        if i > 0:
            pre_color = 'W' if test_board[i-1][0] == 'B' else 'B'
        for j in range(0, 8):
            if j < 7:
                if pre_color == test_board[i][j + 1]:
                    temp += 1
                    test_board[i][j + 1] = 'W' if pre_color == 'B' else 'B'

            if i < 7:
                if pre_color == test_board[i + 1][j]:
                    temp += 1
                    test_board[i + 1][j] = 'W' if pre_color == 'B' else 'B'

            pre_color = 'W' if pre_color == 'B' else 'B'

    return temp


for i in range(0, n - 7):
    for j in range(0, m - 7):
        test_board_1 = [item[j:j + 8] for item in board[i:i + 8]]
        test_board_2 = [item[:] for item in test_board_1]
        res = min(res, check(test_board_1, 'W'), check(test_board_2, 'B'))

print(res)

