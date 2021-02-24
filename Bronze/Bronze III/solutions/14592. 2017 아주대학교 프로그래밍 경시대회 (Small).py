from sys import stdin

arr = []
n = int(stdin.readline().rstrip())

for step in range(n):
    arr.append(list(map(int, stdin.readline().rstrip().split())))

for step in range(n):
    if step == 0:
        s, c, l = arr[step][0], arr[step][1], arr[step][2]
        rank = 1

    elif s < arr[step][0]:
        s, c, l = arr[step][0], arr[step][1], arr[step][2]
        rank = step + 1

    elif c > arr[step][1] and s == arr[step][0]:
        s, c, l = arr[step][0], arr[step][1], arr[step][2]
        rank = step + 1

    elif l > arr[step][2] and s == arr[step][0] and c == arr[step][1]:
        s, c, l = arr[step][0], arr[step][1], arr[step][2]
        rank = step + 1

print(rank)