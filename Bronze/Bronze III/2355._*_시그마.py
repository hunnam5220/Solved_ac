from sys import stdin

arr = list(map(int, stdin.readline().rstrip().split()))
a, b = min(arr), max(arr)

n = b - a

s = (n * (n + 1)) // 2
print(s + (a * (n + 1)))