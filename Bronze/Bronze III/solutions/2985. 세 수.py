from sys import stdin

arr = ['+', '-', '*', '/']
a, b, c = map(str, stdin.readline().rstrip().split())

for step in arr:
    if eval(a + step + b) == int(c):
        print('{}{}{}={}'.format(a, step, b, c))
        break

    elif int(a) == eval(b + step + c):
        print('{}={}{}{}'.format(a, b, step, c))