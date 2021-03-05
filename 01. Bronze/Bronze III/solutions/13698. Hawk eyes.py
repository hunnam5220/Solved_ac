from sys import stdin

shuffle = list(stdin.readline().rstrip())
cups = ['s', 0, 0, 'b']

for step in shuffle:
    if step == 'A':
        tmp = cups[0]
        cups[0] = cups[1]
        cups[1] = tmp

    elif step == 'B':
        tmp = cups[0]
        cups[0] = cups[2]
        cups[2] = tmp

    elif step == 'C':
        tmp = cups[0]
        cups[0] = cups[3]
        cups[3] = tmp

    elif step == 'D':
        tmp = cups[1]
        cups[1] = cups[2]
        cups[2] = tmp

    elif step == 'E':
        tmp = cups[1]
        cups[1] = cups[3]
        cups[3] = tmp

    elif step == 'F':
        tmp = cups[2]
        cups[2] = cups[3]
        cups[3] = tmp

print(cups.index('s')+1)
print(cups.index('b')+1)
