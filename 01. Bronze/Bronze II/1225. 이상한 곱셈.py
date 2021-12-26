from sys import stdin

a, b = stdin.readline().split()
ans = 0
for i in a:
    for j in b:
        ans += (int(i) * int(j))
print(ans)