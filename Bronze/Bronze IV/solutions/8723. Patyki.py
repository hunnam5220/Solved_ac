from sys import stdin

arr = sorted(list(map(int, stdin.readline().rstrip().split())))

if (arr[2] ** 2) == (arr[0]**2 + arr[1] ** 2):
    print(1)

elif arr[0] == arr[1] == arr[2]:
    print(2)

else:
    print(0)