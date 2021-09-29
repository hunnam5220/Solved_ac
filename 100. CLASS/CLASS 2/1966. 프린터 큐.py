from sys import stdin
from collections import deque


for _ in range(int(stdin.readline())):
    q = deque()
    a, b = map(int, stdin.readline().split())
    data = list(map(int, stdin.readline().split()))
    for i in range(a):
        q.append((i, data[i]))

    max_im = max(data)
    res = 0
    while 1:
        document_num, im = q.popleft()
        if max_im > im:
            q.append((document_num, im))
        else:
            res += 1
            if q:
                max_im = max([x[1] for x in q])
            if document_num == b:
                print(res)
                break