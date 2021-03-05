from sys import stdin

x, y = map(int, stdin.readline().split())
lab = 1
cur = x

if cur % (y - x) == 0:
    lab += cur / (y - x)
else:
    lab += cur / (y - x) + 1

print(int(lab))