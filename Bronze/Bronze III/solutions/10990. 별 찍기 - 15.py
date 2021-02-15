from sys import stdin

n = int(stdin.readline().rstrip())
mid = -1

for step in range(1, n + 1):
    if step == 1:
        print(' ' * (n - step) + '*')

    else:
        print(' ' * (n - step) + '*' + ' ' * mid + '*')

    mid += 2