from sys import stdin

for test in range(int(stdin.readline().rstrip())):

    stdin.readline().rstrip()

    sn = 0
    n = int(stdin.readline().rstrip())
    for step in range(n):
        sn += int(stdin.readline().rstrip())

    if sn % n == 0:
        print('YES')
    else:
        print('NO')