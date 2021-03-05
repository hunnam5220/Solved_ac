from sys import stdin

n = int(stdin.readline().rstrip())

result = 0
for step in range(1, n+1):
    tmp = 0
    for x in range(1, step + 1):
        if step % x == 0:
            tmp += 1

    if tmp % 2 != 0:
        tmp += 1

    if tmp // 2 <= 1:
        result += 1
    else:
        result += (tmp // 2)

print(result)