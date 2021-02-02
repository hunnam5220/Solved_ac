from sys import stdin

n = int(stdin.readline().rstrip())

for step in range(n):
    t = int(stdin.readline().rstrip())

    arr = []

    for x in range(1, t):
        for y in range(x, t):
            if x + y == t and x != y:
                arr.append([x, y])

    
