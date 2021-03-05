from sys import stdin

arr = []
n, x, y = map(int, stdin.readline().split())

for step in range(n):
    arr.append(list(map(int, stdin.readline().split())))

x -= 1
y -= 1
k = arr[x][y]
x_1, y_1 = 0, 0

while 1:
    if x_1 != n:
        if arr[x_1][y] > k:
            print('ANGRY')
            break
        else:
            x_1 += 1

    if y_1 != n:
        if arr[x][y_1] > k:
            print('ANGRY')
            break
        else:
            y_1 += 1

    if x_1 == y_1 == n:
        print('HAPPY')
        break