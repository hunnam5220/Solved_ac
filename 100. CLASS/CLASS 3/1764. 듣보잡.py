from sys import stdin
a, b = map(int, stdin.readline().split())
d, bb = set(), set()
for _ in range(a):
    d.add(stdin.readline().rstrip())

for _ in range(b):
    bb.add(stdin.readline().rstrip())

res = set()
res.update(d)
res.update(bb)

res -= (d-bb)
res -= (bb-d)
l = len(res)
print(l)
res = list(res)
res.sort()
for i in range(l):
    print(res[i])