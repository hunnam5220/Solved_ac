from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    v, e = map(int, stdin.readline().rstrip().split())
    print(2 - v + e)