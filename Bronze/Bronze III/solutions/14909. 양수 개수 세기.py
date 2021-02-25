from sys import stdin

arr = list(map(int, stdin.readline().rstrip().split()))
result = 0

for step in arr:
    if step > 0:
        result += 1

print(result)