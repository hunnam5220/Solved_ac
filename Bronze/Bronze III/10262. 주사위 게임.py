from sys import stdin

w, x, y, z = map(int, stdin.readline().rstrip().split())
w1, x1, y1, z1 = map(int, stdin.readline().rstrip().split())

e = len([j for j in range(w, x+1)]) * len([j for j in range(y, z+1)])
g = len([j for j in range(w1, x1+1)]) * len([j for j in range(y1, z1+1)])

if e > g:
    print('Gunnar')
elif e < g:
    print('Emma')
else:
    print('Tie')