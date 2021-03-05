from sys import stdin

d = {0: 'a', 1: 'b', 2: 'c'}
t_c = 1
while 1:

    arr = list(map(int, stdin.readline().rstrip().split()))
    a, b, c = arr

    if arr[0] == arr[1] == arr[2] == 0:
        break

    else:
        if d[arr.index(-1)] == 'c':
            c = ((a ** 2) + (b ** 2)) ** 0.5
            print('Triangle #{}'.format(t_c))
            print('c = %.3f' % c)
            t_c += 1

        elif d[arr.index(-1)] == 'b':
            b = ((c ** 2) - (a ** 2))
            print('Triangle #{}'.format(t_c))
            if b > 0:
                print('b = %.3f' % b ** 0.5)
            else:
                print('Impossible.')
            t_c += 1

        else:
            a = ((c ** 2) - (b ** 2))
            print('Triangle #{}'.format(t_c))
            if a > 0:
                print('a = %.3f' % a ** 0.5)

            else:
                print('Impossible.')
            t_c += 1

    print()
