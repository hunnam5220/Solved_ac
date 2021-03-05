from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    n, k = map(int, stdin.readline().rstrip().split())
    arr = map(int, stdin.readline().rstrip().split())
    result = 0
    for step2 in arr:
        result += int(step2 // k)
    print(result)