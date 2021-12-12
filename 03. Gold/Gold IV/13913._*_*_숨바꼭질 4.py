from collections import deque
from sys import stdin

n, k = map(int, stdin.readline().split())
ways = [-1 for x in range(int(1e5) + 1)]
parent = [0 for x in range(int(1e5) + 1)]


def solve():
    global ans

    q = deque()
    q.append(n)
    ways[n] = 0

    if n == k:
        print(ways[n])
        print(n)
        exit()

    while q:
        now = q.popleft()

        if now == k:
            print(ways[k])
            ans = []
            res = now
            for _ in range(ways[k] + 1):
                ans.append(res)
                res = parent[res]
            print(*ans[::-1])
            break

        for i in [now * 2, now - 1, now + 1]:
            if -1 < i < 100001:
                if ways[i] == -1:
                    ways[i] = ways[now] + 1
                    parent[i] = now
                    q.append(i)


solve()

