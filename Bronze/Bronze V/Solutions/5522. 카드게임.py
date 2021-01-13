from sys import stdin
result = 0
for x in range(5):
    result += int(stdin.readline().rstrip())

print(result)