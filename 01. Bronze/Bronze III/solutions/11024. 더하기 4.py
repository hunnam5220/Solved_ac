from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    print(sum(list(map(int, stdin.readline().rstrip().split()))))