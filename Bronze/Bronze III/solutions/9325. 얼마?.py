from sys import stdin

t = int(stdin.readline().rstrip())

for step in range(t):
    s = int(stdin.readline().rstrip())
    n = int(stdin.readline().rstrip())

    for step2 in range(n):
        q, p = map(int, stdin.readline().rstrip().split())
        s += (q * p)

    print(s)