from sys import stdin

n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())
t = 0
result = 0

for step in range(n):
    a, b = map(int, stdin.readline().rstrip().split())
    if step == 0:
        if t < (m - a + b):
            t = (m - a + b)
    else:
        tmp = t - a + b
        if t < tmp:
            t = t - a + b

    if result < t:
        result = t

print(result)