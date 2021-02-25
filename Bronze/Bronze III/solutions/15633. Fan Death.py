from sys import stdin

n = int(stdin.readline().rstrip())

k = 1
j = n // 2
arr = []

while 1:
    if n % k == 0 and k not in arr:
        arr.append(k)
        if n // k not in arr:
            arr.append((n // k))

    k += 1

    if j < k:
        break

arr = list(set(arr))
arr.sort()
print((sum(arr) * 5) - 24)