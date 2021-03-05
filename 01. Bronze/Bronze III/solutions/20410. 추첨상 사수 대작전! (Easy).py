from sys import stdin

m, seed, x1, x2 = map(int, stdin.readline().rstrip().split())

bp = False

for a in range(1, m):
    for c in range(1, m):
        if (a * seed + c) % m == x1 and (a * x1 + c) % m == x2:
            bp = True
            print(a, c)
            break

    if bp:
        break