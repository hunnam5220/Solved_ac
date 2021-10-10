from sys import stdin

n = int(stdin.readline())
arr = []

for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))

for k in range(n):
    for p in range(n):
        for j in range(n):
            if arr[p][k] and arr[k][j]:
                arr[p][j] = 1
            else:
                arr[p][j] = 0 if arr[p][j] != 1 else 1

for i in range(n):
    print(*arr[i])