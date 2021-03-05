from sys import stdin

result = 0
for step in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())

    result += (b % a)

print(result)