from sys import stdin

arr = []

for step in range(9):
    arr.append(list(map(int, stdin.readline().rstrip().split())))

r, c, m = 0, 0, 0

for step in range(9):
    if m < max(arr[step]):
        r = step + 1
        m = max(arr[step])
        c = arr[step].index(max(arr[step])) + 1

print(m)
print(r, c)