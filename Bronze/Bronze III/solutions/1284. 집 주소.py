from sys import stdin

while True:
    n = stdin.readline().rstrip()
    if n != '0':
        length = 2 + len(n) - 1

        for step in n:
            if step == '1':
                length += 2
            elif step == '0':
                length += 4
            else:
                length += 3

        print(length)
    else:
        break