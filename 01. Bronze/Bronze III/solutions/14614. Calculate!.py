from sys import stdin

a, b, c = map(int, stdin.readline().rstrip().split())

if c % 2 == 0:
    print(a)
else:
    print(a ^ b)