from sys import stdin
print(sum([x ** 5 for x in list(map(int, list(stdin.readline().rstrip())))]))