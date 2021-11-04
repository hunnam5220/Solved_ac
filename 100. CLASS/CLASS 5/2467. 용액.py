from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
res = [arr[0], arr[-1]]
ans = arr[0] + arr[-1]

for i in arr:
    start, end = 0, n
    temp = 0
    while start < end:
        mid = (start + end) // 2
        if abs(arr[mid] + i) < abs(ans) and arr[mid] != i:
            res = [arr[mid], i]
            ans = arr[mid] + i
            start = mid
        else:
            end = mid


print(*list(sorted(res)))