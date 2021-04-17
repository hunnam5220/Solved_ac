from sys import stdin

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().split()))
time = [0 for _ in range(n)]
cnt = 0
idx = 0

while sum(arr) != 0:
    if arr[idx] != 0:
        cnt += 1
        arr[idx] -= 1
        if arr[idx] == 0:
            time[idx] = cnt

    if idx == n - 1:
        idx = 0
    else:
        idx += 1


for x in time:
    print(x, end=' ')
print()