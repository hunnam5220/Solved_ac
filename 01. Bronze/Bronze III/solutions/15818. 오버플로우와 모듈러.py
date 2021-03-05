from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
num = 1
arr = list(map(int, stdin.readline().rstrip().split()))

for step in range(n):
    num *= arr[step]

print(num % m)