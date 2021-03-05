from sys import stdin

n = int(stdin.readline().rstrip())

result = 5
d = 7

if n == 1:
    print(result)

else:
    for x in range(n-1):
        result += d
        d += 3
    print(result % 45678)