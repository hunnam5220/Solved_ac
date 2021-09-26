from sys import stdin
from collections import deque

q = deque()
n = int(stdin.readline())

for _ in range(n):
    command = list(stdin.readline().split())
    if len(command) == 2:
        if command[0] == 'push_back':
            q.append(int(command[1]))

        else:
            q.appendleft(int(command[1]))

    else:
        if command[0] == 'pop_front':
            print(-1) if not q else print(q.popleft())

        if command[0] == 'pop_back':
            print(-1) if not q else print(q.pop())

        if command[0] == 'size':
            print(len(q))

        if command[0] == 'empty':
            print(1) if not q else print(0)

        if command[0] == 'front':
            print(-1) if not q else print(q[0])

        if command[0] == 'back':
            print(-1) if not q else print(q[-1])