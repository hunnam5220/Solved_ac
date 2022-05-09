from sys import stdin

n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
a, b = map(int, stdin.readline().split())

cnt = 0

for p in arr:
    if p - a <= 0:
        cnt += 1
    else:
        cnt += (p - a) // b
        if (p - a) % b != 0:
            cnt += 1

        cnt += 1

print(cnt)