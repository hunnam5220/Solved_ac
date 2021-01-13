from sys import stdin

a, b, k = map(int, stdin.readline().rstrip().split())

if a // k < 3 or b // k < 3:
    print(((a // k) * (b // k)))
else:
    print(((a // k) * (b // k)) - (((a // k) - 2) * ((b // k) - 2)))
