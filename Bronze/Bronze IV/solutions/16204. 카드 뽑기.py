from sys import stdin

n, m, k = map(int, stdin.readline().split())
cnt = 0
forward = [False] * n
back = [True] * n

for x in range(m):
    forward[x] = True

for y in range(n-1, k-1, -1):
    back[y] = False

for a, b in zip(forward, back):
    if a == b:
        cnt += 1

print(cnt)