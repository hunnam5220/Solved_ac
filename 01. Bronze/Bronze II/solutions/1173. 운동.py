from sys import stdin

n, m, M, T, R = map(int, stdin.readline().split())

t, tf = 0, 0
heartbeat = m
while n > 0:
    if tf and heartbeat + T > M:
        t = -1
        break

    if heartbeat + T <= M:
        heartbeat += T
        t += 1
        n -= 1
        tf = 0

    elif heartbeat >= m:
        t += 1
        heartbeat -= R
        if heartbeat < m:
            heartbeat = m
            tf = 1

print(t)
