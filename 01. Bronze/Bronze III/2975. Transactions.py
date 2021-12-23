from sys import stdin

while 1:
    a, b, c = map(str, stdin.readline().rstrip().split())
    if a == '0' and b == 'W' and c == '0':
        break

    if b == 'W':
        temp = int(a) - int(c)
        if temp < -200:
            print('Not allowed')
        else:
            print(temp)

    elif b == 'D':
        temp = int(a) + int(c)
        print(temp)