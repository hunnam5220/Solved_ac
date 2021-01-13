from sys import stdin

arr = list(map(int, stdin.readline().rstrip().split()))

print(arr[0]*arr[1] + arr[2]*arr[3])