from sys import stdin

x = list(stdin.readline().rstrip())
n = str(int(x[0]) * len(x))

while True:
    chk_fa = int(n[0]) * len(n)
    if n == str(chk_fa):
        print('FA')
        break
    else:
        n = str(chk_fa)