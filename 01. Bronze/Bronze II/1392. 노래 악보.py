from sys import stdin

n, m = map(int, stdin.readline().split())

d = {}
ans = []

for i in range(1, n + 1):
    for _ in range(int(stdin.readline())):
        ans.append(i)

for _ in range(m):
    print(ans[int(stdin.readline())])