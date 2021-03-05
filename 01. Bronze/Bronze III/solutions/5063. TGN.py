from sys import stdin

n = int(stdin.readline().rstrip())

for step in range(n):
    r, e, c = map(int, stdin.readline().rstrip().split())

    if (e - c) > r:
        print('advertise')

    elif (e - c) < r:
        print('do not advertise')

    else:
        print('does not matter')