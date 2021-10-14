from sys import stdin
from collections import deque

for _ in range(int(stdin.readline())):
    command = stdin.readline().rstrip()
    n = int(stdin.readline())
    q = deque()

    if n > 0:
        num = list(map(int, stdin.readline()[1:-2].split(',')))
        q.extend(num)
    else:
        num = stdin.readline()[1:-2]

    reverse = False
    pop_cnt, status = 0, ''

    for c in command:
        if c == 'R':
            if 0 < pop_cnt < len(q):
                for k in range(pop_cnt):
                    if reverse:
                        q.pop()
                    else:
                        q.popleft()
                    pop_cnt -= 1

            elif pop_cnt > len(q):
                status = 'error'

            reverse = False if reverse else True
            continue

        if q:
            if c == 'D':
                pop_cnt += 1
            else:
                reverse = False if reverse else True
                continue
        else:
            if c == 'D':
                status = 'error'
                break
            else:
                reverse = False if reverse else True
                continue

    if pop_cnt > 0:
        if 0 < pop_cnt <= len(q):
            for k in range(pop_cnt):
                if reverse:
                    q.pop()
                else:
                    q.popleft()
                pop_cnt -= 1

        elif pop_cnt > len(q):
            status = 'error'

    if status == 'error':
        print(status)
    else:
        if reverse:
            print('['+','.join(map(str, list(q)[::-1]))+']')
        else:
            print('['+','.join(map(str, q))+']')


