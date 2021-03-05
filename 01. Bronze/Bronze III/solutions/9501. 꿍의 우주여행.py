from sys import stdin


for step1 in range(int(stdin.readline().rstrip())):
    n, d = map(int, stdin.readline().rstrip().split())
    result = 0
    for step2 in range(n):
        v, f, c = map(int, stdin.readline().rstrip().split())

        try:
            if d <= (v * f / c):
                result += 1
        except:
            pass

    print(result)