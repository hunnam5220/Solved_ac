from collections import deque
from sys import stdin


def solve(root):
    q = deque()
    q.append(root)
    krr[root] = 1

    while q:
        now = q.popleft()

        for i in arr[now]:
            if krr[i] == 0:
                q.append(i)
                krr[i] = -krr[now]
            else:
                if krr[i] == krr[now]:
                    return False
    return True


for _ in range(int(stdin.readline())):
    v, e = map(int, stdin.readline().split())
    arr = [[] for _ in range(v + 1)]
    krr = [0 for _ in range(v + 1)]
    for __ in range(e):
        a, b = map(int, stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)

    tf = True
    for i in range(1, v + 1):
        if krr[i] == 0:
            if not solve(i):
                tf = False
                break

    print('YES') if tf else print("NO")
