from sys import stdin

for _ in range(int(stdin.readline())):
    y, k = 0, 0
    for __ in range(9):
        a, b = map(int, stdin.readline().split())
        y += a
        k += b
    if y > k:
        print("Yonsei")
    elif k > y:
        print('Korea')
    else:
        print('Draw')
