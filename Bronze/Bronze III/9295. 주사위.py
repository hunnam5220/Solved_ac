from sys import stdin

t = int(stdin.readline().rstrip())

for step in range(t):
    print("Case {}: {}".format(step + 1, sum(list(map(int, stdin.readline().rstrip().split())))))