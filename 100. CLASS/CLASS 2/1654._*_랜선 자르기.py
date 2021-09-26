from sys import stdin

k, n = map(int, stdin.readline().split())
arr = []
for _ in range(k):
    arr.append(int(stdin.readline()))

x = max(arr)
start = 1
end = x

while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in range(k):
        temp += arr[i] // mid

    if temp < n:
        end = mid - 1

    else:
        start = mid + 1

print(end)