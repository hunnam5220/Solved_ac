from sys import stdin

for step in range(3):
    arr = []
    x = int(stdin.readline().rstrip())
    for step1 in range(x):
        arr.append(int(stdin.readline().rstrip()))
    s = sum(arr)

    if s == 0:
        print(0)
    elif s < 0:
        print('-')
    else:
        print('+')
