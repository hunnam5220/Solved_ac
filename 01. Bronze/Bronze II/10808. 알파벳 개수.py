from sys import stdin

d = {chr(x + 97): 0 for x in range(26)}

for i in stdin.readline().rstrip():
    d[i] += 1

print(*d.values())