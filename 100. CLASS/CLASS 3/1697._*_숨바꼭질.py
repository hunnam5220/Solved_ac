from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
visited = [0 for _ in range(100001)]


def solve(s):
    q = deque()
    q.append(s)

    while q:
        x = q.popleft()
        if x == k:
            return visited[x]

        for next_x in (x * 2, x - 1, x + 1):
            if 0 <= next_x <= 10 ** 5 and not visited[next_x]:
                visited[next_x] = visited[x] + 1
                q.append(next_x)


print(solve(n))