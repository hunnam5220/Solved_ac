from sys import stdin

a = list(map(int, stdin.readline().rstrip().split()))
c = list(map(int, stdin.readline().rstrip().split()))

print(c[0]-a[2], c[1]//a[1], c[2]- a[0])