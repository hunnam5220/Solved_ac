from sys import stdin

n = int(stdin.readline().rstrip())

for step in range(1, n + 1):
    print(' ' * (n - step) + ' '.join(['*' for x in range(step)]))