from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())
    p = 0

    if 1 == a:
        p += 500
    elif 1 < a <= 3:
        p += 300
    elif 3 < a <= 6:
        p += 200
    elif 6 < a <= 10:
        p += 50
    elif 10 < a <= 15:
        p += 30
    elif 15 < a <= 21:
        p += 10

    if 1 == b:
        p += 512
    elif 1 < b <= 3:
        p += 256
    elif 3 < b <= 7:
        p += 128
    elif 7 < b <= 15:
        p += 64
    elif 15 < b <= 31:
        p += 32

    print(p * 10000)