from sys import stdin

res = []

for _ in range(int(stdin.readline())):
    x = int(stdin.readline())
    if x == 0:
        res.pop()
        continue
    res.append(x)

print(sum(res))