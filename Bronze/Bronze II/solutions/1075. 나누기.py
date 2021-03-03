from sys import stdin

n = int(stdin.readline().rstrip())
f = int(stdin.readline().rstrip())

if n == f:
    print(str(n)[-2:])
else:
    s = n // 100
    t = '00'

    tmp = str(s) + str(t)
    num = (int(tmp) // f) * f
    while 1:
        if int(tmp) <= num:
            print(str(num)[-2:])
            break
        else:
            num += f

