from sys import stdin

case = 1
while 1:
    n0 = int(stdin.readline().rstrip())

    if n0 == 0:
        break

    else:
        n1 = n0 * 3

        if n1 % 2 == 0:
            print('{}. even'.format(case), end=' ')
            case += 1
            n2 = n1 / 2
        else:
            print('{}. odd'.format(case), end=' ')
            case += 1
            n2 = (n1 + 1) / 2

        print(int(3 * n2 // 9))