from sys import stdin

for i in range(int(stdin.readline())):
    n, s, d = map(int, stdin.readline().split())
    temp = s * d
    answer = 0

    for _ in range(n):
        di, vi = map(int, stdin.readline().split())
        if di <= temp:
            answer += vi

    print("Data Set {}:\n{}".format(i + 1, answer))
    print()