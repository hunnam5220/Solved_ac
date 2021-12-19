from sys import stdin


while 1:
    n = stdin.readline().rstrip()
    if not n:
        break
    n = int(n)
    res = '1'

    while int(res) % n != 0:
        res += '1'

    print(len(res))