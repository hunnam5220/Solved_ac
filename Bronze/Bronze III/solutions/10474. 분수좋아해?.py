from sys import stdin

while 1:
    a, b = map(int, stdin.readline().rstrip().split())

    if a == b == 0:
        break

    else:
        print('{} {} / {}'.format(a // b, a % b, b))