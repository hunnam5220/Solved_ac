from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    n, num = map(int, stdin.readline().rstrip().split())

    onum = True
    for chk in str(num):
        if int(chk) >= 8:
            onum = 0
            break

    if onum != 0:
        onum = int(('0o' + str(num)), 8)

    hnum = int('0x' + str(num), 16)
    print('{} {} {} {}'.format(n, onum, num, hnum))