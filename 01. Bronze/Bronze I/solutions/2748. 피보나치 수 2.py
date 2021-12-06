from sys import stdin

arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

n = int(stdin.readline())

if n < 18:
    print(arr[n])
else:
    for i in range(18, 91):
        arr.append(arr[i - 2] + arr[i - 1])

    print(arr[n])