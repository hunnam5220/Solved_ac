from sys import stdin

t = int(stdin.readline().rstrip())

for step in range(t):
    n = int(stdin.readline().rstrip())

    p1, p2= [0], [0]

    for i in range(n):
        p, pp = stdin.readline().rstrip().split()

        if p == pp:
            pass

        elif (p == 'R' and pp == 'P') or (p == 'S' and pp == 'R') or (p == 'P' and pp == 'S'):
            p2.append(1)

        elif (p == 'R' and pp == 'S') or (p == 'S' and pp == 'P') or (p == 'P' and pp == 'R'):
            p1.append(1)

    if sum(p1) > sum(p2):
        print('Player 1')

    elif sum(p1) < sum(p2):
        print('Player 2')

    else:
        print('TIE')