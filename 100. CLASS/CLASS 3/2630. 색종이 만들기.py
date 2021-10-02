from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 9)

n = int(stdin.readline())
board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))


def solve(code, mode, new_board):
    temp = 0
    b_sum = 0
    for i in range(mode):
        b_sum += sum(new_board[i])

    if mode == 1:
        for i in range(mode):
            for j in range(mode):
                if new_board[i][j] == code:
                    temp += 1
        return temp

    if (b_sum != mode ** 2 and code == 1) or (b_sum != 0 and code == 0):
        sep_board_1 = [x[:mode // 2] for x in new_board[:mode // 2]]
        sep_board_2 = [x[mode // 2:] for x in new_board[:mode // 2]]
        sep_board_3 = [x[:mode // 2] for x in new_board[mode // 2:]]
        sep_board_4 = [x[mode // 2:] for x in new_board[mode // 2:]]

        temp += solve(code, mode // 2, sep_board_1)
        temp += solve(code, mode // 2, sep_board_2)
        temp += solve(code, mode // 2, sep_board_3)
        temp += solve(code, mode // 2, sep_board_4)
    else:
        return temp + 1

    return temp


mode = n
res0 = solve(0, mode, board)
res1 = solve(1, mode, board)

print(res0)
print(res1)

"""
4
1 0 0 1
0 0 0 0
0 0 0 0
1 0 0 1
"""