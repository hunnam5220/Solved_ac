from sys import stdin

a, b = map(str, stdin.readline().split())
print(bin(int(a, 2) + int(b, 2))[2:])
