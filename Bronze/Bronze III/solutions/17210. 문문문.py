from sys import stdin

n = int(stdin.readline().rstrip())
method = int(stdin.readline().rstrip())

if n >= 6:
    print('Love is open door')
else:
    for step in range(1, n):
        if method == 1:
            print(0)
            method = 0
        else:
            print(1)
            method = 1