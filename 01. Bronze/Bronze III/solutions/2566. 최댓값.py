from sys import stdin

arr = []

for step in range(9):
    arr.append(list(map(int, stdin.readline().rstrip().split())))

ans = ()
max_val = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] >= max_val:
            max_val = arr[i][j]
            ans = (i + 1, j + 1)

print(max_val)
print(*ans)