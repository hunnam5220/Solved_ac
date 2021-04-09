from sys import stdin

n, c = map(int, stdin.readline().split())
arr = []

for step in range(n):
    arr.append(int(stdin.readline().rstrip()))

arr.sort()
start = 1
end = arr[-1] - arr[0]
result = 0

while end >= start:
    mid = (start + end) // 2

    value = arr[0]
    cnt = 1

    for i in range(1, n):
        if arr[i] >= value + mid:
            value = arr[i]
            cnt += 1

    if cnt >= c:
        start = mid + 1
        result = mid

    else:
        end = mid - 1

print(result)