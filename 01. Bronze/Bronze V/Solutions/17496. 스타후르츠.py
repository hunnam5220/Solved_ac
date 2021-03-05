from sys import stdin

n, t, c, p = map(int, stdin.readline().rstrip().split())

print((n-1)//t * c * p)