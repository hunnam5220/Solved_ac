from sys import stdin

cups = [True, False, False]

m = int(stdin.readline().rstrip())

for step in range(m):
    x, y = map(int, stdin.readline().split())
    tmp = cups[x-1]
    cups[x - 1] = cups[y - 1]
    cups[y - 1] = tmp

for t in range(len(cups)):
    if cups[t] is True:
        print(t+1)