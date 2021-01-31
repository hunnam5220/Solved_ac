from sys import stdin

arr = sorted(list(map(int, stdin.readline().rstrip().split())))

if (arr[1] - arr[0]) != (arr[2] - arr[1]):

    if arr[1] - arr[0] > arr[2] - arr[1]:
        print((arr[0] + arr[2] - arr[1]))
    else:
        print((arr[1] + arr[1] - arr[0]))

else:
    print((arr[2] + arr[1] - arr[0]))