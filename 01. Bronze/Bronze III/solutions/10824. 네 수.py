from sys import stdin

a, b, c, d = map(str, stdin.readline().rstrip().split())

print(eval((a + b)+'+'+(c + d)))