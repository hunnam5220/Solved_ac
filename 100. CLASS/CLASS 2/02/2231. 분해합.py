from sys import stdin

n = int(stdin.readline())
res = 0

for i in range(1, n + 1):
    k = i + sum(list(map(int, list(str(i)))))
    if k == n:
        res = i
        break

print(res)