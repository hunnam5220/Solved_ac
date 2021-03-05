from sys import stdin

n, b = map(int, stdin.readline().rstrip().split())
bit = 1

for x in range(1, b+1):
    bit += (2 ** x)

if n > bit:
    print('no')
else:
    print('yes')