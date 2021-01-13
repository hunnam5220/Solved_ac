from sys import stdin

n, w, h, l = map(int, stdin.readline().split())
w //= l
h //= l

x = w * h

if n < x:
    print(n)
else:
    print(x)