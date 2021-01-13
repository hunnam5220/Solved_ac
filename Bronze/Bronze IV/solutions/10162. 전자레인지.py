from sys import stdin

n = int(stdin.readline().rstrip())

arr = [300, 60, 10]

result = []

for step in range(3):
    result.append(n // arr[step])
    n %= arr[step]
if n > 0:
    print(-1)
else:
    for step in range(3):
        print(result[step], end=' ')