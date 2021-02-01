from sys import stdin

n = int(stdin.readline().rstrip())
while 1:
    k = int(stdin.readline().rstrip())

    if k == 0:
        break
    else:
        if k % n == 0:
            print('{} is a multiple of {}.'.format(k, n))
        else:
            print('{} is NOT a multiple of {}.'.format(k, n))