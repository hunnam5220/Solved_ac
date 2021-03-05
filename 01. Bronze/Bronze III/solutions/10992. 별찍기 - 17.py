from sys import stdin

n = int(stdin.readline().rstrip())
stars = n * 2 - 1
mid = -1
for step in range(1, n + 1):
    if step == 1:
        print(' ' * (n-1) + '*')
        mid += 2

    elif step == n:
        print('*' * stars)

    else:
        space = ' ' * (n - step)
        print(space + '*' + ' ' * mid + '*')
        mid += 2