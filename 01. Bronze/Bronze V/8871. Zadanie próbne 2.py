from sys import stdin

print(sum([x * 5 for x in list(map(int, stdin.readline().split()))]))