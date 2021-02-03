from sys import stdin

n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())
result, t = 0, 0

for step in range(n):
    a, b = map(int, stdin.readline().rstrip().split())
    if step == 0:
        if m + a - b < 0:
            result = 0
            break

        elif t < (m + a - b):
            t = (m + a - b)
    else:
        t += a - b
        if t < 0:
            result = 0
            break

    if t > result:
        result = t

print(result)