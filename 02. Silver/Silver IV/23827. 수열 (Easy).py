from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
r = 0
s = sum(a)
for i in range(n):
    r += a[i] * (s - a[i])

print((r // 2) % 1000000007)