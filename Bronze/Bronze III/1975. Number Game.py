from sys import stdin


def solution(n, x, arr):
    if n < x:
        arr.append(n)
        return arr

    if n % x == 0:
        arr.append(0)
        return solution(n // x, x, arr)

    else:
        arr.append(1)
        return solution(n // x, x, arr)


def chk_zero(arr, idx, cnt):
    if arr[idx] == 0:
        return chk_zero(arr, idx + 1, cnt + 1)
    else:
        return cnt


t = int(stdin.readline().rstrip())

for step in range(t):
    n = int(stdin.readline().rstrip())
    idx, cnt = 0, 1
    if n % 2 == 0 and n > 20:
        for x in range(2, n // 2):
            arr = []
            if n % x == 0:
                cnt = chk_zero(solution(n, x, arr), idx, cnt)

    elif n == 1:
        cnt = 0

    else:
        for x in range(2, n):
            arr = []
            if n % x == 0:
                tmp_arr = solution(n, x, arr)
                cnt = chk_zero(tmp_arr, idx, cnt)

    print(cnt)
