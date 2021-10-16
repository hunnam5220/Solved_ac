from sys import stdin
from collections import deque


def f(n, m):
    global res
    q = deque()
    q.append((n, ''))

    while q:
        num, com = q.popleft()

        if num == m:
            res = com
            return

        # D
        temp = (int(num) * 2) % 10000
        while len(str(temp)) < 4:
            temp = '0' + str(temp)

        if not visited[int(temp)]:
            q.append((str(temp), com + 'D'))
            visited[int(temp)] = True

        # S
        temp = 9999 if int(num) - 1 < 0 else int(num) - 1
        while len(str(temp)) < 4:
            temp = '0' + str(temp)
        if not visited[int(temp)]:
            q.append((str(temp), com + 'S'))
            visited[int(temp)] = True


        # L
        temp = num[1:] + num[0]
        if not visited[int(temp)]:
            q.append((str(temp), com + 'L'))
            visited[int(temp)] = True

        # R
        temp = num[-1] + num[:-1]
        if not visited[int(temp)]:
            q.append((temp, com + 'R'))
            visited[int(temp)] = True


for _ in range(int(stdin.readline())):
    n, m = stdin.readline().rstrip().split()
    while len(n) < 4:
        n = '0' + n
    while len(m) < 4:
        m = '0' + m

    res = ''
    visited = [False for _ in range(10001)]
    f(n, m)
    print(res)