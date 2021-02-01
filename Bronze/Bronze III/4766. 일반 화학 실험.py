from sys import stdin

n = float(stdin.readline().rstrip())

while 1:
    k = float(stdin.readline().rstrip())

    if k == 999:
        break
    else:
        print('%.2f' % (k - n))
        n = k