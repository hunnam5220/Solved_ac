from sys import stdin

n = int(stdin.readline())
temp = n * (n - 1) // 2
s = list(stdin.readline().rstrip())


def check(arr):
    idx = 0
    for i in range(n):
        data = arr[i]
        if i == 0 and idx == 0:
            if s[idx] == '-':
                if arr[i] >= 0:
                    return False
            elif s[idx] == '0':
                if arr[i] != 0:
                    return False
            elif s[idx] == '+':
                if arr[i] <= 0:
                    return False

            idx += 1

        for j in range(i + 1, n):
            data += arr[j]
            if s[idx] == '-':
                if data >= 0:
                    return False
            elif s[idx] == '0':
                if data != 0:
                    return False
            elif s[idx] == '+':
                if data <= 0:
                    return False
            idx += 1
    return True


def solve(arr):
    if len(arr) == n:
        if not check(arr):
            return
        else:
            print(*arr)
            exit()

    for i in range(-10, 11):
        solve(arr + [i])


for i in range(-10, 11):
    if s[0] == '-':
        solve([i])
