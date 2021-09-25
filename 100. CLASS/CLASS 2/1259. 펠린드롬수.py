from sys import stdin


while 1:
    n = list(stdin.readline().rstrip())
    if n == ['0']:
        break
    else:
        a = n[:]
        n.reverse()
        print('yes' if n == a else 'no')