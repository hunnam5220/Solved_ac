from sys import stdin

while 1:
    a, b, c, d = map(int, stdin.readline().rstrip().split())
    a, b, c, d = int(a), int(b), int(c), int(d)

    h, j = sorted([a, b]), sorted([c, d])

    if a == b == c == d == 0:
        break
    else:
        print(abs(max(h) - min(j)), end=' ')
        print(abs(min(h) - max(j)))