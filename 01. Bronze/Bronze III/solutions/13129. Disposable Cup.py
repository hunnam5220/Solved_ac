from sys import stdin

a, b, n = map(int, stdin.readline().rstrip().split())
high = (a + b) * n
arr = [high]
for step in range(1, n):
    high -= b
    arr.append(high)

arr.sort()
print(' '.join(map(str, arr)))