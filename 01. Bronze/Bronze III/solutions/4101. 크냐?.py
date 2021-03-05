from sys import stdin


while 1:
    a, b = map(int, stdin.readline().rstrip().split())

    if a == 0 and b == 0:
        break

    else:
        if a > b:
            print('Yes')
        else:
            print('No')

