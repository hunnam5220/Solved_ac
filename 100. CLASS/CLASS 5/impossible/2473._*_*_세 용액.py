from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
data.sort()

ans, res = [], int(1e11)


for i in range(n - 2):
    m = data[i]
    start, end = i + 1, n - 1
    while start < end:
        value = data[start] + data[end] + m
        if abs(value) < res:
            res = abs(value)
            ans = [data[start], data[end], m]

        if value < 0:
            start += 1

        elif value > 0:
            end -= 1

        else:
            ans.sort()
            print(*ans)
            exit()

ans.sort()
print(*ans)