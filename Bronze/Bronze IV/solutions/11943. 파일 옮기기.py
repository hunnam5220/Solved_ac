from sys import stdin

arr1 = list(map(int, stdin.readline().split()))
arr2 = list(map(int, stdin.readline().split()))

print(min([(arr1[0] + arr2[1]), arr1[1] + arr2[0]]))