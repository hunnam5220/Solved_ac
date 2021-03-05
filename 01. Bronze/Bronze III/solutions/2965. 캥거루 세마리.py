from sys import stdin

arr = sorted(list(map(int, stdin.readline().rstrip().split())))

i = arr[1] - arr[0]
k = arr[2] - arr[1]

if i > k:
    print(i - 1)
else:
    print(k - 1)