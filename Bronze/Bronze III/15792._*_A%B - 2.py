from sys import stdin

a, b = map(int, stdin.readline().rstrip().split())
result = str(a // b) + '.'
a = (a % b) * 10

for step in range(1000):
    result += str(a // b)
    a = (a % b) * 10

print(result)