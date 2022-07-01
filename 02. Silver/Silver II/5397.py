from sys import stdin

for _ in range(int(stdin.readline())):
    string = stdin.readline().rstrip()
    left, right = [], []

    for s in string:
        if s == '>':
            if right:
                left.append(right.pop())

        elif s == '<':
            if left:
                right.append(left.pop())

        elif s == '-':
            if left:
                left.pop()

        else:
            left.append(s)

    print(''.join(left + list(reversed(right))))