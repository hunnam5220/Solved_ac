from sys import stdin, setrecursionlimit
setrecursionlimit(10000000)

n = int(stdin.readline().rstrip())
arr = []
chk = True

for step in range(3):
    arr.append(list(map(int, stdin.readline().rstrip().split())))

for step in range(100000 + 1):
    a = step
    d = arr[0][0] - a
    e = arr[2][1] - d
    b = arr[1][0] - e
    c = arr[0][1] - b
    f = arr[2][0] - c

    if a >= 0 and b >= 0 and c >= 0 and d >= 0 and e >= 0 and f >= 0:
        print(1)
        print(a, d)
        print(b, e)
        print(c, f)
        chk = False
        break

if chk:
    print(0)