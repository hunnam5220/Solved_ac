from sys import stdin
from collections import deque

q = deque()

for i in range(int(stdin.readline())):
    command = list(stdin.readline().split())
    if len(command) == 2:
        q.append(int(command[1]))

    else:
        if command[0] == 'front':
            if not q:
                print(-1)
            else:
                print(q[0])

        elif command[0] == 'back':
            if not q:
                print(-1)
            else:
                print(q[-1])

        elif command[0] == 'empty':
            print(0) if q else print(1)

        elif command[0] == 'size':
            print(len(q))

        elif command[0] == 'pop':
            if not q:
                print(-1)
            else:
                print(q.popleft())