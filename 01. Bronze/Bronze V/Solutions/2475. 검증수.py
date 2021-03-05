from sys import stdin
arr = list(map(int, stdin.readline().rstrip().split()))

arr = [x ** 2 for x in arr]

print(sum(arr) % 10)