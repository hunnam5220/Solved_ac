from sys import stdin

while 1:
    a, b, c = map(int, stdin.readline().rstrip().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if (b - a) == (c - b) and (b - a) != 0:
            print('AP', c + (b - a))
        else:
            print('GP', int(c * (b / a)))