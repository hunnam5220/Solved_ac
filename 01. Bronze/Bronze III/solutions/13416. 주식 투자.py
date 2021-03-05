from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    result = 0
    for days in range(int(stdin.readline().rstrip())):
        cost = max(list(map(int, stdin.readline().rstrip().split())))
        if cost > 0:
            result += cost
    print(result)