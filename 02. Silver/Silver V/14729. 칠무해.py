from sys import stdin

q = []
n = int(stdin.readline())
for _ in range(n):
    q.append(float(stdin.readline()))

q.sort()
for x in range(7):
    print('%.3f' % q[x])