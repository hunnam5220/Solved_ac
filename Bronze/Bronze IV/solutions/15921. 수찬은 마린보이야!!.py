from sys import stdin

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().rstrip().split()))
average = 0
hwak = 0
if n != 0:
    for x in arr:
        average += x
        hwak += x / n

    print("%.2f" % ((average / n) / hwak))
else:
    print('divide by zero')