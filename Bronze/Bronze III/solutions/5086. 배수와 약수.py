from sys import stdin


while 1:
    a, b = map(int, stdin.readline().rstrip().split())
    if a == b == 0:
        break

    else:
        if a < b:
            if b % a == 0:
                print('factor')
            else:
                print('neither')

        elif a > b:
            if a % b == 0:
                print('multiple')
            else:
                print('neither')