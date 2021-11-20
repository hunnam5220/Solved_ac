from sys import stdin

n, s = map(int, stdin.readline().split())
data = list(map(int, stdin.readline().split()))
arr = [0] * (n + 1)
for i in range(1, n + 1):
    arr[i] += arr[i-1] + data[i - 1]

ans = int(1e9)

print(data)
print(arr)

start, end = 0, 1
while start != n:
    if arr[end] - arr[start] >= s:
        if end - start < ans:
            ans = end - start
        start += 1
    else:
        if end != n:
            end += 1
        else:
            start += 1

print(ans) if ans != int(1e9) else print(0)