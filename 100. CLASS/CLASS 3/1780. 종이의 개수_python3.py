from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))


def check(r, c, mode):
    for i in range(r, r + mode):
        for j in range(c, c + mode):
            if arr[r][c] != arr[i][j]:
                return False
    return True


def solve(r, c, mode):
    if check(r, c, mode):
        res[arr[r][c] + 1] += 1
    else:
        for i in range(r, r + mode, mode // 3):
            for j in range(c, c + mode, mode // 3):
                solve(i, j, mode // 3)


res = [0, 0, 0]
solve(0, 0, n)
for i in range(3):
    print(res[i])
