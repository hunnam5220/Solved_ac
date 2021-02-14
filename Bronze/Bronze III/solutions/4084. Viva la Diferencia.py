from sys import stdin

cnt = 0
while 1:
    a, b, c, d = map(int, stdin.readline().rstrip().split())

    if a == b == c == d == 0:
        break
    else:
        while 1:
            if a == b == c == d:
                print(cnt)
                cnt = 0
                break
            else:
                tmp = a
                a = abs(a - b)
                b = abs(b - c)
                c = abs(c - d)
                d = abs(d - tmp)
                cnt += 1