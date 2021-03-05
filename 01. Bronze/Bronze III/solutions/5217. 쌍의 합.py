from sys import stdin

n = int(stdin.readline().rstrip())

for step in range(n):
    t = int(stdin.readline().rstrip())

    string = ''

    for x in range(1, t):
        for y in range(x, t):
            if x + y == t and x != y:
                if string == '':
                    string += '%d %d' % (x, y)

                elif string != '' and string[-1] != ',':
                    string += ', %d %d' % (x, y)

    print('Pairs for {}: '.format(t) + string)