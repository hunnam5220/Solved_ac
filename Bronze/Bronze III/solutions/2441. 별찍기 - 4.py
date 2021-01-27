from sys import stdin

n = int(stdin.readline().rstrip())
for step in range(n, 0, -1):
    print(' '*(n-step) + ('*' * step))