from sys import stdin
for _ in range(int(stdin.readline())):
    data = list(stdin.readline().split())
    n = float(data[0])
    for i in data[1:]:
        if i == '@':
            n *= 3
        elif i == '#':
            n -= 7
        elif i == '%':
            n += 5
    print('%.2f' % n)