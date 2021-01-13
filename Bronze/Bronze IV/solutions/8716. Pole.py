from sys import stdin

x1, y1, x2, y2 = map(int, stdin.readline().rstrip().split())
x3, y3, x4, y4 = map(int, stdin.readline().rstrip().split())

if x2 < x3 or x1 > x4:
    print(0)
else:
    a = abs(sorted([x1, x2, x3, x4])[1] - sorted([x1, x2, x3, x4])[2])
    b = abs(sorted([y1, y2, y3, y4])[1] - sorted([y1, y2, y3, y4])[2])
    print(a * b)