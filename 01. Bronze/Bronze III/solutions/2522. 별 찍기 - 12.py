from sys import stdin

n = int(stdin.readline().rstrip())
s = n - 1

for x in range(1, n+1):
    print(' ' * s + '*' * x)
    s -= 1

s += 2
for x in reversed(range(1, n)):
    print(' ' * s + '*' * x)
    s += 1