from sys import stdin

n = int(stdin.readline().rstrip())
result = 1
p = 2
if n > 8:
    k = n // 3 - 3

    for step in range(k):
        result += p
        p += 1

    print(result)
else:
    print(0)