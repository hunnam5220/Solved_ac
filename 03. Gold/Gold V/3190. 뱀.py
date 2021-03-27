from sys import stdin
from collections import deque
q = deque()
q.append([0, 0])


def move_snake(i, j):
    if i >= n or j >= n or i < 0 or j < 0 or arr[i][j] == 9:
        return False

    if arr[i][j] != 0:
        q.append([i, j])
        arr[i][j] = 9
        return True

    elif arr[i][j] == 0:
        a, b = q.popleft()
        arr[i][j] = 9
        q.append([i, j])
        arr[a][b] = 0
        return True


n = int(stdin.readline().rstrip())
arr = [[0] * n for _ in range(n)]
arr[0][0] = 9
time, idx, chk = 0, 0, True
i, j = 0, 0

for step in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().split())
    arr[a - 1][b - 1] = 1
l = int(stdin.readline().rstrip())
for step in range(l):
    x, c = stdin.readline().split()

    if chk:
        while 1:
            time += 1
            if idx == 0:
                j += 1

            elif idx == 1:
                i += 1

            elif idx == 2:
                j -= 1

            else:
                i -= 1

            if not move_snake(i, j):
                print(time)
                chk = False
                break

            if time == int(x):
                if c == 'D':
                    idx += 1
                    if idx >= 4:
                        idx = 0
                else:
                    idx -= 1
                    if idx <= -1:
                        idx = 3

                if step != l - 1:
                    break




"""
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
>> 9

10
4
1 2
1 3
1 4
1 5
4 
8 D
10 D
11 D
13 L
>> 21

10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
>> 13
"""