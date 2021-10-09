from sys import stdin

n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))


def solve(board, chk, mode):
    res = 0
    if mode == 1:
        return 1 if board[0][0] == chk else 0

    tf = True
    for i in range(mode):
        if board[i].count(chk) != mode:
            tf = False
            break

    if tf:
        return 1
    else:
        res += solve([item[:(mode // 3)] for item in board[:(mode // 3)]], chk, mode // 3)
        res += solve([item[:(mode // 3)] for item in board[(mode // 3):(mode // 3) * 2]], chk, mode // 3)
        res += solve([item[:(mode // 3)] for item in board[(mode // 3) * 2:]], chk, mode // 3)

        res += solve([item[(mode // 3):(mode // 3) * 2] for item in board[:(mode // 3)]], chk, mode // 3)
        res += solve([item[(mode // 3):(mode // 3) * 2] for item in board[(mode // 3):(mode // 3) * 2]], chk, mode // 3)
        res += solve([item[(mode // 3):(mode // 3) * 2] for item in board[(mode // 3) * 2:]], chk, mode // 3)

        res += solve([item[(mode // 3) * 2:] for item in board[:(mode // 3)]], chk, mode // 3)
        res += solve([item[(mode // 3) * 2:] for item in board[(mode // 3):(mode // 3) * 2]], chk, mode // 3)
        res += solve([item[(mode // 3) * 2:] for item in board[(mode // 3) * 2:]], chk, mode // 3)

    return res


answer = []
for v in [-1, 0, 1]:
    res = 0
    l = solve(arr, v, n)
    print(l)
