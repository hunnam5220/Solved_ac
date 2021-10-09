from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, list(stdin.readline().rstrip()))))
answer = ''


def check(x, y, mode):
    for i in range(x, x + mode):

        for j in range(y, y + mode):
            if arr[x][y] != arr[i][j]:
                return False
    return True


def solve(x, y, mode):
    global answer

    if check(x, y, mode):
        if arr[x][y] == 1:
            answer += str(1)
        else:
            answer += str(0)
    else:
        answer += str('(')
        solve(x, y, mode // 2)
        solve(x, y + mode // 2, mode // 2)
        solve(x + mode // 2, y, mode // 2)
        solve(x + mode // 2, y + mode // 2, mode // 2)
        answer += str(')')




solve(0, 0, n)
print(answer)