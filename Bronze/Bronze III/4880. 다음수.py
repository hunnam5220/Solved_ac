from sys import stdin

a, b, c = map(int, stdin.readline().rstrip().split())

if abs(abs(a)-abs(b)) == abs(abs(b)-abs(c)):
    