from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())
    g = 3
    result = 1

    for x in range(1, a // b):
        result += g
        g += 2

    print(result)