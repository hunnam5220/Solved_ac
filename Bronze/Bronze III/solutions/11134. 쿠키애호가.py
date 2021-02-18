from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    n, c = map(int, stdin.readline().rstrip().split())
    result = n // c
    if n % c == 0:
        print(result)
    else:
        print(result + 1)