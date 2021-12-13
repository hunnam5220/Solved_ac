from sys import stdin

for _ in range(int(stdin.readline())):
    for s in list(stdin.readline().split()):
        data = list(reversed(s))
        print(*data, sep='', end=' ')
    print()