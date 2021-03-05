from sys import stdin

a, b = map(int, stdin.readline().split())

if b > 0:
    print(a // b)
    print(a % b)
else:
    print(-1*(a // (-1*b)))
    print((a % (-1*b)))