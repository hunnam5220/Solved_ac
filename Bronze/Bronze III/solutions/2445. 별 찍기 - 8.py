from sys import stdin

n = int(stdin.readline().rstrip())

for step in range(n):
    print('*' * (step+1) + ' ' * (n * 2 - (step+1)*2) + '*' * (step+1))

for step in range(n-2, -1, -1):
    print('*' * (step+1) + ' ' * (n * 2 - (step+1)*2) + '*' * (step+1))