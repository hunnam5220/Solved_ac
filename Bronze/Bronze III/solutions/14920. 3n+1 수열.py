from sys import stdin

cn = int(stdin.readline().rstrip())
n = 1

if cn != 1:
    while 1:
        if cn % 2 == 0:
            cn //= 2

        else:
            cn = 3 * cn + 1

        n += 1

        if cn == 1:
            print(n)
            break
else:
    print(1)