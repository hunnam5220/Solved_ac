from sys import stdin

d = sum(list(map(int, stdin.readline().rstrip().split())))
m = sum(list(map(int, stdin.readline().rstrip().split())))

if d > m: print(d)
else: print(m)
