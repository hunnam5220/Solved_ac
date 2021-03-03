from sys import stdin

n, x, k = map(int, stdin.readline().rstrip().split())

arr = [0] * n
arr[x-1] = 1

for step in range(k):
    a, b = map(int, stdin.readline().rstrip().split())
    tmp = arr[a - 1]
    arr[a - 1] = arr[b - 1]
    arr[b - 1] = tmp

print(arr.index(1) + 1)