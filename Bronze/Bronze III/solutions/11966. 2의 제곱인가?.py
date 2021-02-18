from sys import stdin

n = int(stdin.readline().rstrip())
a = 0

while 1:
    if n == 1:
        print(1)
        break

    elif 1 < n < 2:
        print(0)
        break

    else:
        n /= 2