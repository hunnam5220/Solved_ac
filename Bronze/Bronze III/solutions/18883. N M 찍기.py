from sys import stdin

arr = []
n, m = map(int, stdin.readline().rstrip().split())

for step in range(n):
    arr.append([x for x in range(m * step + 1, (step + 1) * m + 1)])

for step in arr:
    print(' '.join(map(str, step)))
