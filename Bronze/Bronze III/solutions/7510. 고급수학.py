from sys import stdin

n = int(stdin.readline().rstrip())

for step in range(n):
    a, b, c = map(int, stdin.readline().rstrip().split())
    print('Scenario #{}:'.format(step + 1))

    if a == b == c == 1:
        print('no')

    elif (a ** 2) == ((b ** 2) + (c ** 2)):
        print('yes')

    elif (b ** 2) == ((c ** 2) + (a ** 2)):
            print('yes')

    elif (c ** 2) == ((b ** 2) + (a ** 2)):
        print('yes')

    else:
        print('no')

    print()