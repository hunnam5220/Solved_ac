from sys import stdin
arr = list(map(int, stdin.readline().split()))

print(int(max([arr[0] * arr[1] / arr[2], arr[0] / arr[1] * arr[2]])))