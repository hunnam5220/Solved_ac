from sys import stdin

n = int(stdin.readline().rstrip())

for x in range(n):
    pay = float(stdin.readline().rstrip())

    discount = pay * 0.2

    print('$%.2f' % round((pay - discount), 2))