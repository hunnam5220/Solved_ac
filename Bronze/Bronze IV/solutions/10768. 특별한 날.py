from sys import stdin

m, d = int(stdin.readline().rstrip()), int(stdin.readline().rstrip())

if m < 2:
    print('Before')
elif m > 2:
    print('After')
else:
    if d > 18:
        print('After')
    elif d < 18:
        print('Before')
    else:
        print('Special')