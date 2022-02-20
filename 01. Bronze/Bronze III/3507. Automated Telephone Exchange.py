from sys import stdin

n = int(stdin.readline())
ans = 0
for i in range(1, 100):
    for j in range(1, 100):
        if n - i - j == 0:
            ans += 1
        if n - i - j < 0:
            break
print(ans)