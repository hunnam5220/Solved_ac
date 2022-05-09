from sys import stdin

d = {x: False for x in range(1, 31)}
ans = []
for i in range(28):
    d[int(stdin.readline())] = True

for key, val in d.items():
    if not val:
        ans.append(key)

ans.sort()
print(*ans, sep='\n')