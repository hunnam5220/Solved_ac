from sys import stdin

t = int(stdin.readline().rstrip())

cost = {
    'a': 350.34, 'b': 230.90, 'c': 190.55, 'd': 125.30, 'e': 180.90
}

for step in range(t):
    a, b, c, d, e = map(int, stdin.readline().rstrip().split())

    print('$%.2f' % (a * cost['a'] + b * cost['b'] + c * cost['c'] + d * cost['d'] + e * cost['e']))