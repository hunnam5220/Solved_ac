from sys import stdin

a, b = map(int, stdin.readline().rstrip().split())
arr = []

for x in range(1, a+1):
    if a % x == 0:
        arr.append(x)

    if len(arr) == b:
        break

if len(arr) < b:
    print(0)

else:
    print(arr[b-1])