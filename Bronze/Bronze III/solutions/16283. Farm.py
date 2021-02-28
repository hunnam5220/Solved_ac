from sys import stdin

a, b, n, w = map(int, stdin.readline().rstrip().split())
arr = []
y = 1

while 1:
    if y == n:
        break
    else:
        if y * a + (n - y) * b == w:
            arr.append([y, n-y])
        y += 1

if len(arr) > 1 or len(arr) == 0:
    print(-1)
else:
    print(' '.join(map(str, arr[0])))