from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
result = n // 1
if m != 1:
    result += n // m
    k = n // m

    while 1:
        if k >= m:
            result += k // m
            k = k // m
        else:
            break
print(result)