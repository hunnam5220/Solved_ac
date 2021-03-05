from sys import stdin

s, t, d = map(int, stdin.readline().split())

print(int(((d / (s * 2)) * t)))