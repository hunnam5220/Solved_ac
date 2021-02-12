from sys import stdin

n, t = map(int, stdin.readline().rstrip().split())
over, cnt = 0, 0
come = list(map(int, stdin.readline().rstrip().split()))

for step in come:
    if over + step > t:
        break

    else:
        over += step
        cnt += 1

print(cnt)