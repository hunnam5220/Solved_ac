from sys import stdin

m, n = map(int, stdin.readline().rstrip().split())

if m == 2:
    print(2)
else:
    if m > n:
        print(n * 2 - 1)
    elif m < n:
        print((m-1) * 2)
    elif n == m:
        print((n-1) * 2)