from sys import stdin

while 1:
    try:
        a, b, c = map(int, stdin.readline().rstrip().split())

        if b-a >= c-b:
            print(b-a-1)

        elif b-a < c-b:
            print(c-b-1)

    except:
        break