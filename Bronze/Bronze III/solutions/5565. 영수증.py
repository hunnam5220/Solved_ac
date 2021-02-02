from sys import stdin
print(int(stdin.readline().rstrip()) - sum([int(stdin.readline().rstrip()) for x in range(9)]))