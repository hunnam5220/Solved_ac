from sys import stdin

t = int(stdin.readline().rstrip())

for step in range(t):
    n = list(reversed(bin(int(stdin.readline().rstrip()))[2:]))

    for x in n:
        if x == '1':
            chk = n.index(x)
            print(chk, end=' ')
            n[chk] = False