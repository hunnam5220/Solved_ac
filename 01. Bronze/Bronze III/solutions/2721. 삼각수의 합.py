from sys import stdin

t = int(stdin.readline().rstrip())
for step in range(t):
    n = int(stdin.readline().rstrip())
    result = 0

    for x in range(1, n+1):
        result += sum([i for i in range(1, x+2)]) * x

    print(result)