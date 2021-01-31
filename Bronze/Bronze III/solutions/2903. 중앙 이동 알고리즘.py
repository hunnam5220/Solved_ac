from sys import stdin

n = int(stdin.readline().rstrip())
s = 5
if n == 1:
    print(9)
elif n == 2:
    print(25)
else:
    for step in range(n - 2):
        s = s + s - 1

    print(s ** 2)