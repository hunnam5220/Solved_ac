from sys import stdin

arr = list(stdin.readline().rstrip())
cups = [True, False, False]

for step in arr:
    if step == 'A':
        tmp = cups[0]
        cups[0] = cups[1]
        cups[1] = tmp

    elif step == 'B':
        tmp = cups[1]
        cups[1] = cups[2]
        cups[2] = tmp

    else:
        tmp = cups[0]
        cups[0] = cups[2]
        cups[2] = tmp

print(cups.index(True)+1)