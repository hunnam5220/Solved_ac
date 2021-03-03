from sys import stdin

n, t = map(int, stdin.readline().rstrip().split())
result = 0
m = 0

for step in range(t):
    if m == 0:
        result += 1
        if result == n * 2:
            m = 1
    elif m == 1:
        result -= 1
        if result == 1:
            m = 0

print(result)