from sys import stdin

n = int(stdin.readline().rstrip())

print(int(n - (n * 0.22)), end=' ')
print(int(n - ((n * 0.2) * 0.22)), end=' ')