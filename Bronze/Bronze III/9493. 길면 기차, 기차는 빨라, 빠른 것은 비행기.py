from sys import stdin

while 1:
    m, a, b = map(int, stdin.readline().rstrip().split())
    m, a, b = m * 1000, a * 1000 / 3600, b * 1000 / 3600

    if m == a == b == 0:
        break

    else:
        print((m / a))
        print((m / b))