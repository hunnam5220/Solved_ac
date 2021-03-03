from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    n, m = map(int, stdin.readline().rstrip().split())
    arr = []
    if n < 12 or m < 4:
        print(-1)
    else:
        for step1 in range(n):
            arr.append([x for x in range(m * step1 + 1, m * (step1 + 1) + 1)])
        print(arr[11][3])