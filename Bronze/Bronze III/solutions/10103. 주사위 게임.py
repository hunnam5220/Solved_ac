from sys import stdin

c, s = 100, 100

for step in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())

    if a == b:
        pass
    elif a > b:
        s -= a
    else:
        c -= b

print(c)
print(s)
