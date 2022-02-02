from sys import stdin

bingo_tf = [[False] * 5 for _ in range(5)]
bingo_board = []
num_xy = {}


def find_bingo():
    cnt = 0
    for i in range(5):
        if False in bingo_tf[i]:
            continue
        else:
            cnt += 1

    for i in range(5):
        state = True
        for j in range(5):
            if bingo_tf[j][i] is False:
                state = False
                break
        if state:
            cnt += 1

    state = True
    for i in range(5):
        if bingo_tf[i][i] is False:
            state = False
            break

    if state:
        cnt += 1

    state = True
    for i, j in zip(range(5), range(4, -1, -1)):
        if bingo_tf[i][j] is False:
            state = False
            break

    if state:
        cnt += 1

    return True if cnt >= 3 else False


for i in range(5):
    data = list(map(int, stdin.readline().split()))
    bingo_board.append(data)
    for j in range(5):
        num_xy[data[j]] = (i, j)

ans = 0
for i in range(5):
    data = list(map(int, stdin.readline().split()))
    for j in range(5):
        call_number = data[j]
        x, y = num_xy[call_number]
        bingo_tf[x][y] = True

        ans += 1
        if ans >= 12:
            if find_bingo():
                print(ans)
                exit()

"""
18

14 12 5 11 13 
9 4 3 8 25 
18 15 19 24 20 
1 6 7 23 17 
22 16 10 2 21 
17 11 9 24 6 
23 1 2 15 12 
8 14 21 10 16 
3 22 18 13 25 
4 5 19 7 20
"""
