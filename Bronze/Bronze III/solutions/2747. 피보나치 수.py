from sys import stdin

arr = [0, 1]

for step in range(45):
    arr.append(sum(arr[-2:]))

print(arr[int(stdin.readline().rstrip())])