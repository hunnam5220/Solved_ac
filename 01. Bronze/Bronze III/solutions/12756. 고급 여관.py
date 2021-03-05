from sys import stdin

a_at, a_life = map(int, stdin.readline().rstrip().split())
b_at, b_life = map(int, stdin.readline().rstrip().split())

a_dead = b_life // a_at
b_dead = a_life // b_at

if b_life % a_at != 0:
    a_dead += 1
if a_life % b_at != 0:
    b_dead += 1

if a_dead < b_dead:
    print('PLAYER A')
elif a_dead > b_dead:
    print('PLAYER B')
else:
    print('DRAW')