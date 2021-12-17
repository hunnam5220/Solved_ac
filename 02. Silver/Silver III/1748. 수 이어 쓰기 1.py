from sys import stdin

n = int(stdin.readline())
l = len(str(n))
ans = 0
k = 9
for i in range(l - 1):
    ans += k * (10 ** i) * (i + 1)

ans += ((n + 1) - 10 ** (l - 1)) * l
print(ans)