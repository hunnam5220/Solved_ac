from sys import stdin

k = int(stdin.readline().rstrip())
d1, d2 = map(int, stdin.readline().rstrip().split())

if d1 == d2:
    print(k ** 2)
elif d1 == d2 * 3:
    print((k ** 2 - d2 ** 2))
else:
    a, b = max([d1, d2]), min([d1, d2])
    h = k ** 2 - (((a - b) / 2) ** 2)
    print(h)