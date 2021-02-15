from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    d, n, s, p = map(int, stdin.readline().rstrip().split())
    b = d+n*p
    j = n*s
    if b == j:
        print('does not matter')
    elif b > j:
        print('do not parallelize')
    else:
        print('parallelize')