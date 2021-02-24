from sys import stdin

a, b = map(int, stdin.readline().rstrip().split())
result = 1

for step in range(a, b + 1):
    tmp = 0
    for x in range(1, step + 1):
        tmp += x

    result *= tmp

print(result % 14579)