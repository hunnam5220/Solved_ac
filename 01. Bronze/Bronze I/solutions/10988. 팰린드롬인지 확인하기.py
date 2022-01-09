from sys import stdin

s = list(stdin.readline().rstrip())
r = list(reversed(s))
if s == r:
    print(1)
else:
    print(0)