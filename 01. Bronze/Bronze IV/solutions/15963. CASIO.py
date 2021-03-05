from sys import stdin

a, b = map(int, stdin.readline().split())

if a == b:
    print(1)
else:
    print(0)