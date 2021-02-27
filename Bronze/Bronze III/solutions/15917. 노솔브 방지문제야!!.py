from sys import stdin

q = int(stdin.readline().rstrip())

for step in range(q):
    n = int(stdin.readline().rstrip())
    if n == 1 or n % 2 == 0:
        if '1' in bin(n)[3:]:
            print(0)
        else:
            print(1)
    else:
        print(0)