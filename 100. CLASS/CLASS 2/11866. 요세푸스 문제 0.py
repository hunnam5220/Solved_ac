from sys import stdin
from collections import deque

res = []
n, k = map(int, stdin.readline().split())
q = deque()
q.extend([x for x in range(1, n + 1)])

cnt = 0
while 1:
    if cnt != k - 1:
        cnt += 1
        q.append(q.popleft())
        continue

    res.append(q.popleft())
    n -= 1
    cnt = 0

    if not q:
        print('<' + ', '.join(map(str, res)) + '>')
        break