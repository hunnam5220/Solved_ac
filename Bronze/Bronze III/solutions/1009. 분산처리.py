from sys import stdin

n = int(stdin.readline().rstrip())

for step in range(n):
    a, b = map(int, stdin.readline().rstrip().split())

    if b % 4 == 0:
        b = 4
    else:
        b %= 4

    if (a ** b) % 10 == 0:
        print(10)
    else:
        print((a ** b) % 10)