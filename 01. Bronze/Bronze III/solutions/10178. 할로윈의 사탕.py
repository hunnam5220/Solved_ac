from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())

    print("You get {} piece(s) and your dad gets {} piece(s).".format(int(a // b), int(a % b)))