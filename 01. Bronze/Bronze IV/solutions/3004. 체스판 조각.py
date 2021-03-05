from sys import stdin
n = int(stdin.readline().rstrip())
h = 1
w = 1

if n % 2 == 0:
    h += n // 2
    w += n // 2
    print(h*w)

else:
    h += n // 2
    w += (n // 2) + 1
    print(h * w)

