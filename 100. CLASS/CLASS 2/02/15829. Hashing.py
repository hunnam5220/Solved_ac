from sys import stdin

d = {chr(x + 96): x for x in range(1, 27)}

n = int(stdin.readline())
arr = list(stdin.readline())
res = 0

for i in range(n):
    res += d[arr[i]] * (31 ** i)

print(res % 1234567891)