from sys import stdin

n = int(stdin.readline().rstrip())

xw, yw = 0, 0
for step in range(n):
    x, y = map(int, stdin.readline().rstrip().split())

    if x > y:
        xw += 1
    elif x < y:
        yw += 1

print(xw, yw)