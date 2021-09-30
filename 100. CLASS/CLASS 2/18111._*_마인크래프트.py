from sys import stdin

n, m, b = map(int, stdin.readline().split())
arr = []
height = 0

for i in range(n):
    data = list(map(int, stdin.readline().split()))
    arr.append(data)
    k = max(data)
    height = max(height, k)


def solve(new_board, height, inven):
    t = 0
    blocks = n * m
    nc = 0
    for i in range(n):
        for j in range(m):
            y = height - new_board[i][j]
            if y > 0:
                if inven >= y:
                    t += 1 * y
                    inven -= 1 * y
                    blocks -= 1
                    continue
                else:
                    nc += y
                    blocks -= 1
                    continue

            elif y < 0:
                y = new_board[i][j] - height
                t += 2 * y
                inven += y
                blocks -= 1
                continue

            else:
                blocks -= 1
                continue

    inven -= nc
    t += nc

    if blocks == 0 and inven >= 0:
        return t
    else:
        return -1


res = [int(1e9), 0]
for h in range(height + 1):
    k = solve(arr, h, b)
    if k == -1:
        continue

    if k <= res[0]:
        res[0] = k
        if res[1] < h:
            res[1] = h


print(*res)