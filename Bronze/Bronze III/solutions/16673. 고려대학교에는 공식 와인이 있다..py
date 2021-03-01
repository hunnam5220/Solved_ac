from sys import stdin

c, k, p = map(int, stdin.readline().rstrip().split())
result = 0

for n in range(1, c+1):
    result += k * n + p * (n ** 2)

print(result)