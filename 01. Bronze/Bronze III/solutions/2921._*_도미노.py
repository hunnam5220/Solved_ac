from sys import stdin

n = int(stdin.readline().rstrip())

result = 3
g = 6
p = 3

if n == 1:
    print(result)
else:
    for step in range(1, n):
        result += p + g
        p += g
        g += 3

    print(result)