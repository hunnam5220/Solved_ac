from sys import stdin

n = int(stdin.readline())
arr = []

for b in range(n):
    a, c = stdin.readline().split()
    arr.append((int(a), b, c))

arr.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(arr[i][0], arr[i][2])
