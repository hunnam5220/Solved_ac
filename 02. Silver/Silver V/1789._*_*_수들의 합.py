from sys import stdin

k = int(stdin.readline())
ans, num, res = 0, 1, 0

while res < k:
    res += num
    num += 1
    ans += 1

if res == k:
    print(ans)
else:
    print(ans - 1)