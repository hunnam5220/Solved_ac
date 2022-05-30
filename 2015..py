from sys import stdin
from collections import defaultdict

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
prefix = defaultdict(int)
ans = 0

for i in range(1, n):
    arr[i] += arr[i - 1]

for i in range(n):
    if arr[i] == k:
        ans += 1
    ans += prefix[arr[i] - k]
    prefix[arr[i]] += 1

print(ans)