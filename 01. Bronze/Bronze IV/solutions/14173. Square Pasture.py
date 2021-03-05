from sys import stdin

x1, y1, x2, y2 = map(int, stdin.readline().split())
x3, y3, x4, y4 = map(int, stdin.readline().split())
x = [x1, x2, x3, x4]
y = [y1, y2, y3, y4]
tmpx = max(x) - min(x)
tmpy = max(y) - min(y)
print(max([tmpx, tmpy]) ** 2)