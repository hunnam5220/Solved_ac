from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    result = 0
    n, m = map(int, stdin.readline().rstrip().split())

    for x in range(1, n - 1):
        for y in range(x + 1, n):
            tmp = (((x ** 2) + (y ** 2) + m) / (x * y))
            if tmp == int(tmp):
                result += 1

    print(result)
