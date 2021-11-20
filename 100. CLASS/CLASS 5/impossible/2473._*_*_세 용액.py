from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
data.sort()

ans, res = [], int(1e11)


# 왼쪽을 고정해놓고 포인터를 움직인다.
# 가운데, 오른쪽이 움직이면서 탐색할 것.
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

        # 합이 0일 때 이다.
        # 아무거나 출력하라고 했으니까 아무거나 출력하고 종료한다.
        else:
            ans.sort()
            print(*ans)
            exit()

ans.sort()
print(*ans)