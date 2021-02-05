from sys import stdin

try:
    while 1:
        m, p, l, e, r, s, n = map(int, stdin.readline().rstrip().split())

        for step in range(n):
            t_m = p // s
            t_p = l // r
            t_l = m * e

            m = t_m
            p = t_p
            l = t_l

        print(m)
except:
    exit()