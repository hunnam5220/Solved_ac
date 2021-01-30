from sys import stdin

n = int(stdin.readline().rstrip())

for x in range(1, n+1):
    print('*' * x)

for x in reversed(range(1, n)):
    print('*' * x)