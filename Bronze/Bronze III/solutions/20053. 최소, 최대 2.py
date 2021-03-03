from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().split()))
    print(min(arr), max(arr))