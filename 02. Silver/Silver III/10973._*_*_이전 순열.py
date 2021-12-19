from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
k, p = -1, -1

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        k = i

if k == -1:
    print(-1)
    exit()

for i in range(k + 1, n):
    if arr[i] < arr[k]:
        p = i

arr[k], arr[p] = arr[p], arr[k]
temp = arr[k + 1:]
temp.sort(reverse=True)
ans = arr[:k + 1] + temp
print(*ans)