from sys import stdin

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().rstrip().split()))
g, result = 1, 0

for step in range(n):
    if arr[step] == 1:
        result += g
        g += 1
    else:
        g = 1

print(result)