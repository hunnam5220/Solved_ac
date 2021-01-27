from sys import stdin

result = 1
for step in range(int(stdin.readline().rstrip())):
    result += int(stdin.readline().rstrip()) - 1

print(result)