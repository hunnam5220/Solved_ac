from sys import stdin

n, a, b = map(int, stdin.readline().rstrip().split())

for step in range(n):
    k = int(stdin.readline().rstrip())

    if a >= k or b >= k or (((a ** 2) + (b ** 2)) ** 0.5) >= k:
        print('DA')
    else:
        print('NE')