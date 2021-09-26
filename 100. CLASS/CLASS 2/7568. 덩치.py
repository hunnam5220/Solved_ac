from sys import stdin

arr = []
n = int(stdin.readline())

for i in range(n):
    a, b = map(int, stdin.readline().split())
    arr.append([1, a, b])

for i in range(n):
    wi, hi = arr[i][1:]
    for j in range(n):
        if i != j:
            wj, hj = arr[j][1:]
            if wi > wj and hi > hj:
                arr[j][0] += 1

for i in arr:
    print(i[0], end=' ')
