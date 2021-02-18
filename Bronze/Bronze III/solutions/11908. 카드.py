from sys import stdin

n = int(stdin.readline().rstrip())
print(sum(list(sorted(list(map(int, stdin.readline().rstrip().split()))))[:-1]))