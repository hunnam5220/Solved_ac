from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())
    print('{} {}'.format((b * 2 - a), b - (b * 2 - a)))
