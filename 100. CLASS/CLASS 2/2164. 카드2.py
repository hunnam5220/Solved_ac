from sys import stdin
from collections import deque
n = int(stdin.readline())
arr = deque()
arr.extend([x for x in range(1, n + 1)])
TF = 1

while 1:
    if len(arr) > 1 and TF:
        arr.popleft()
        TF = 0
        n -= 1
    else:
        a = arr.popleft()
        arr.append(a)
        TF = 1

    if n == 1:
        print(arr[0])
        break