from sys import stdin

while 1:
    m, a, b = map(int, stdin.readline().rstrip().split())
    m, a, b = m, a / 3600, b / 3600

    if m == a == b == 0:
        break

    else:
        tmp = abs(round(m / a - m / b))

        h = 0
        m = int(tmp // 60)
        s = int(tmp % 60)

        if m >= 60:
            h = int(m // 60)
            m = int(m % 60)

        print('{}:{:02}:{:02}'.format(h, m, s))