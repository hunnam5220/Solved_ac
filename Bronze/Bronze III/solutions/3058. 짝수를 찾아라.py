from sys import stdin

t = int(stdin.readline().rstrip())

for step in range(t):
    arr = list(map(int, stdin.readline().rstrip().split()))
    brr = [x for x in arr if x % 2 == 0]
    print(sum(brr), min(brr))