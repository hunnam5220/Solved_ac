from sys import stdin

N = int(stdin.readline().rstrip())

print(int(N * (N - 1) * (N - 2) * (N - 3) / 24))