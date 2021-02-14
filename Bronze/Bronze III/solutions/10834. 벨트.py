from sys import stdin

cycle = 1
k = 1

for step in range(int(stdin.readline().rstrip())):
    a, b, c = map(int, stdin.readline().rstrip().split())

    if c == 1:
        if cycle:
            cycle = 0
        else:
            cycle = 1

    k = (k / a) * b

if cycle:
    print(0, int(k))
else:
    print(1, int(k))