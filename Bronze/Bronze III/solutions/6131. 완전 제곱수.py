from sys import stdin

n = int(stdin.readline().rstrip())
result = 0

for b in range(1, 501):
    for a in range(1, 501):
        if (a ** 2) == ((b ** 2) + n):
            result += 1

print(result)