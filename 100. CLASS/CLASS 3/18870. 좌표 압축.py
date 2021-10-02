from sys import stdin

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
a = list(set(data))
a.sort()
d = {}
res = []
for i in range(len(a)):
    d[a[i]] = i

for i in data:
    res.append(d[i])

print(*res)