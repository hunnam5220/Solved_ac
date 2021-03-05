from sys import stdin

n, m, k = map(int, stdin.readline().rstrip().split())
result = 0

if 0 < n and 0 < m:
    for x in range(k):
        if m * 2 > n:
            m -= 1
        else:
            n -= 1

    while True:
        if n < 2 or m < 1:
            break

        if n >= 2:
            n -= 2
            if m >= 1:
                m -= 1
                result += 1

print(result)