from sys import stdin

arr = []
for step in range(7):
    n = int(stdin.readline().rstrip())
    if n % 2 != 0:
        arr.append(n)

if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)
