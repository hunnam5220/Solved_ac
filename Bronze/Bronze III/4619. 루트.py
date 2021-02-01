from sys import stdin

while 1:
    b, n = map(int, stdin.readline().rstrip().split())

    if b == 0 and n == 0:
        break

    else:
        s = 9999999999999999

        for step in range(1, 10000000000):
            k = abs(b - (step ** n))
            if s > k:
                s = k
                result = step
            else:
                break

    print(result)