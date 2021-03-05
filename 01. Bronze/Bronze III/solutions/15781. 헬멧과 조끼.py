from sys import stdin

n, m = map(int, stdin.readline().split())

print((max(list(map(int, stdin.readline().split()))) + max(list(map(int, stdin.readline().split())))))