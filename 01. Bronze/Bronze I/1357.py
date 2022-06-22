from sys import stdin

x, y = stdin.readline().rstrip().split()
print(int(str(int(x[::-1]) + int(y[::-1]))[::-1]))