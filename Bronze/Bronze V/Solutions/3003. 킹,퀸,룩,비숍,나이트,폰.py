from sys import stdin

arr = list(map(int, stdin.readline().rstrip().split()))

std = [1, 1, 2, 2, 2, 8]

for x in range(len(arr)):
    print(std[x]-arr[x], end=' ')