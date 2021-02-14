from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    d = int(stdin.readline().rstrip())
    s = 1
    while 1:
        t = s ** 2
        if s == 1 and s + t > d:
            print(0)
            break

        if s + t > d:
            print(s-1)
            break
        else:
            s += 1