from sys import stdin

while True:
    arr = list(map(int, stdin.readline().split()))
    g = 1
    if arr[0] == 0:
        break

    for x in range(1, len(arr)):
        if x % 2 == 0:
            g -= arr[x]
        else:
            g *= arr[x]
    print(g)